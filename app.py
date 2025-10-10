from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="CarDealer Pro API", description="Premium Car Dealership Backend API")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
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

# Sample car data
cars_data = [
    Car(
        id=1,
        make="Toyota",
        model="Camry",
        year=2022,
        price=28500,
        mileage=15000,
        color="Silver",
        fuel_type="Hybrid",
        transmission="CVT",
        engine="2.5L 4-Cylinder",
        features=["Leather Seats", "Sunroof", "Navigation", "Backup Camera", "Bluetooth"],
        image_url="/static/images/2024-Toyota-Camry-rendering-front.jpg",
        description="Excellent condition Toyota Camry with low mileage and premium features."
    ),
    Car(
        id=2,
        make="Honda",
        model="Accord",
        year=2023,
        price=32000,
        mileage=8000,
        color="White",
        fuel_type="Gasoline",
        transmission="Automatic",
        engine="1.5L Turbo 4-Cylinder",
        features=["Heated Seats", "Apple CarPlay", "Android Auto", "Lane Assist", "Blind Spot Monitor"],
        image_url="/static/images/2018_Honda_Accord_Touring.jpg",
        description="Nearly new Honda Accord with advanced safety features and modern technology."
    ),
    Car(
        id=3,
        make="BMW",
        model="3 Series",
        year=2021,
        price=45000,
        mileage=25000,
        color="Black",
        fuel_type="Gasoline",
        transmission="Automatic",
        engine="2.0L Turbo 4-Cylinder",
        features=["Premium Sound", "Leather Interior", "Sport Package", "Heated Seats", "Navigation"],
        image_url="/static/images/BMW-rendering-front.jpg",
        description="Luxury BMW 3 Series with sport package and premium amenities."
    ),
    Car(
        id=4,
        make="Mercedes-Benz",
        model="C-Class",
        year=2022,
        price=52000,
        mileage=18000,
        color="Blue",
        fuel_type="Gasoline",
        transmission="Automatic",
        engine="2.0L Turbo 4-Cylinder",
        features=["MBUX Infotainment", "Panoramic Sunroof", "Premium Leather", "Burmester Audio", "AMG Package"],
        image_url="/static/images/Mercedes-Benz-2024.jpg",
        description="Sophisticated Mercedes-Benz C-Class with AMG styling and advanced technology."
    ),
    Car(
        id=5,
        make="Audi",
        model="A4",
        year=2023,
        price=48000,
        mileage=12000,
        color="Gray",
        fuel_type="Gasoline",
        transmission="Automatic",
        engine="2.0L Turbo 4-Cylinder",
        features=["Virtual Cockpit", "Bang & Olufsen Audio", "Quattro AWD", "Adaptive Cruise", "Parking Assist"],
        image_url="/static/images/Audi-2024.jpg",
        description="Premium Audi A4 with Quattro all-wheel drive and cutting-edge technology."
    ),
    Car(
        id=6,
        make="Tesla",
        model="Model 3",
        year=2023,
        price=55000,
        mileage=5000,
        color="Red",
        fuel_type="Electric",
        transmission="Automatic",
        engine="Electric Motor",
        features=["Autopilot", "Supercharging", "Premium Interior", "Over-the-Air Updates", "Full Self-Driving Capable"],
        image_url="/static/images/Tesla-2024.jpg",
        description="Revolutionary Tesla Model 3 with advanced autopilot and electric performance."
    )
]

# API Routes

@app.get("/api/cars", response_model=List[Car])
async def get_cars():
    return cars_data

@app.get("/api/cars/{car_id}", response_model=Car)
async def get_car(car_id: int):
    car = next((car for car in cars_data if car.id == car_id), None)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@app.post("/api/search", response_model=List[Car])
async def search_cars(search: CarSearch):
    filtered_cars = cars_data.copy()
    
    if search.make:
        filtered_cars = [car for car in filtered_cars if car.make.lower() == search.make.lower()]
    
    if search.model:
        filtered_cars = [car for car in filtered_cars if car.model.lower() == search.model.lower()]
    
    if search.min_price:
        filtered_cars = [car for car in filtered_cars if car.price >= search.min_price]
    
    if search.max_price:
        filtered_cars = [car for car in filtered_cars if car.price <= search.max_price]
    
    if search.min_year:
        filtered_cars = [car for car in filtered_cars if car.year >= search.min_year]
    
    if search.max_year:
        filtered_cars = [car for car in filtered_cars if car.year <= search.max_year]
    
    if search.fuel_type:
        filtered_cars = [car for car in filtered_cars if car.fuel_type.lower() == search.fuel_type.lower()]
    
    if search.transmission:
        filtered_cars = [car for car in filtered_cars if car.transmission.lower() == search.transmission.lower()]
    
    return filtered_cars

@app.get("/api/featured", response_model=List[Car])
async def get_featured_cars():
    """Get featured cars (first 3 cars)"""
    return cars_data[:3]

@app.get("/api/makes")
async def get_car_makes():
    """Get all unique car makes"""
    makes = list(set(car.make for car in cars_data))
    return {"makes": sorted(makes)}

@app.get("/api/models/{make}")
async def get_car_models(make: str):
    """Get all models for a specific make"""
    models = list(set(car.model for car in cars_data if car.make.lower() == make.lower()))
    return {"models": sorted(models)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True)
