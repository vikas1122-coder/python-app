from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
from pymongo import ReturnDocument
import uvicorn
from dotenv import load_dotenv
import os
# from motor.motor_asyncio import AsyncIOMotorClient

from database import db, init_db


app = FastAPI()


print("Current working directory: ", os.getcwd())
if load_dotenv():  # picks up .env in the project root
    print("✅ Loaded .env file")
else:
    print("❌ .env file not found")

# Static assets (images, css, js under /static)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Serve frontend asset folders
app.mount("/css", StaticFiles(directory="frontend/css"), name="css")
app.mount("/js", StaticFiles(directory="frontend/js"), name="js")
app.mount("/images", StaticFiles(directory="frontend/images"), name="frontend-images")


# ---------------- Models ----------------
class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int
    price: int
    mileage: int
    color: str
    fuel_type: str
    transmission: str
    engine: str
    features: List[str]
    image_url: str
    description: str

class CarSearch(BaseModel):
    make: Optional[str] = None
    model: Optional[str] = None
    min_price: Optional[int] = None
    max_price: Optional[int] = None
    min_year: Optional[int] = None
    max_year: Optional[int] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None

def doc_to_car(doc) -> dict:
    """Convert Mongo doc to Car shape (drop _id)."""
    if not doc:
        return None
    d = dict(doc)
    d.pop("_id", None)
    return d

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- API Routes ----------------

# List all cars
@app.get("/api/cars", response_model=List[Car])
async def get_cars():
    cursor = db.cars.find({})
    return [doc_to_car(d) async for d in cursor]

# Get one car by numeric id
@app.get("/api/cars/{car_id}", response_model=Car)
async def get_car(car_id: int):
    doc = await db.cars.find_one({"id": car_id})
    if not doc:
        raise HTTPException(status_code=404, detail="Car not found")
    return doc_to_car(doc)

# Create car (enforces unique numeric id)
@app.post("/api/cars", response_model=Car)
async def create_car(car: Car):
    existing = await db.cars.find_one({"id": car.id})
    if existing:
        raise HTTPException(status_code=409, detail="Car with that id already exists")
    await db.cars.insert_one(car.dict())
    return car

# Update car by numeric id
@app.put("/api/cars/{car_id}", response_model=Car)
async def update_car(car_id: int, car: Car):
    res = await db.cars.find_one_and_update(
        {"id": car_id},
        {"$set": car.dict()},
        return_document=ReturnDocument.AFTER,
    )
    if not res:
        raise HTTPException(status_code=404, detail="Car not found")
    return doc_to_car(res)

# Delete car by numeric id
@app.delete("/api/cars/{car_id}")
async def delete_car(car_id: int):
    res = await db.cars.delete_one({"id": car_id})
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Car not found")
    return {"message": "Car deleted"}

# Search cars
@app.post("/api/cars/search", response_model=List[Car])
async def search_cars(search: CarSearch):
    q: dict = {}

    if search.make:
        q["make"] = search.make
    if search.model:
        q["model"] = search.model
    if search.fuel_type:
        q["fuel_type"] = search.fuel_type
    if search.transmission:
        q["transmission"] = search.transmission

    if search.min_price is not None or search.max_price is not None:
        q["price"] = {}
        if search.min_price is not None:
            q["price"]["$gte"] = search.min_price
        if search.max_price is not None:
            q["price"]["$lte"] = search.max_price
        if not q["price"]:
            q.pop("price")

    if search.min_year is not None or search.max_year is not None:
        q["year"] = {}
        if search.min_year is not None:
            q["year"]["$gte"] = search.min_year
        if search.max_year is not None:
            q["year"]["$lte"] = search.max_year
        if not q["year"]:
            q.pop("year")

    cursor = db.cars.find(q)
    return [doc_to_car(d) async for d in cursor]

# Featured cars
@app.get("/api/featured", response_model=List[Car])
async def get_featured_cars():
    cursor = db.cars.find({}).sort("year", -1).limit(3)
    return [doc_to_car(d) async for d in cursor]

# Makes & models
@app.get("/api/makes")
async def get_car_makes():
    makes = await db.cars.distinct("make")
    return {"makes": sorted(makes)}

@app.get("/api/models/{make}")
async def get_car_models(make: str):
    models = await db.cars.distinct("model", {"make": make})
    return {"models": sorted(models)}

# Serve index.html at root
@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.on_event("startup")
async def _startup():
    await init_db()
    print("db initilized")


# ---------------- Main ----------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
