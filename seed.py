# seed.py
import asyncio
from database import db


cars = [
    {
        "id": 1,
        "make": "Toyota",
        "model": "Camry",
        "year": 2022,
        "price": 28500,
        "mileage": 15000,
        "color": "Silver",
        "fuel_type": "Hybrid",
        "transmission": "CVT",
        "engine": "2.5L 4-Cylinder",
        "features": ["Leather Seats", "Sunroof", "Navigation", "Backup Camera", "Bluetooth"],
        "image_url": "/static/images/2024-Toyota-Camry-rendering-front.jpg",
        "description": "Excellent condition Toyota Camry with low mileage and premium features."
    },
    {
        "id": 2,
        "make": "Honda",
        "model": "Accord",
        "year": 2023,
        "price": 32000,
        "mileage": 8000,
        "color": "White",
        "fuel_type": "Gasoline",
        "transmission": "Automatic",
        "engine": "1.5L Turbo 4-Cylinder",
        "features": ["Heated Seats", "Apple CarPlay", "Android Auto", "Lane Assist", "Blind Spot Monitor"],
        "image_url": "/static/images/2018_Honda_Accord_Touring.jpg",
        "description": "Nearly new Honda Accord with advanced safety features and modern technology."
    },
    {
        "id": 3,
        "make": "BMW",
        "model": "3 Series",
        "year": 2021,
        "price": 45000,
        "mileage": 25000,
        "color": "Black",
        "fuel_type": "Gasoline",
        "transmission": "Automatic",
        "engine": "2.0L Turbo 4-Cylinder",
        "features": ["Premium Sound", "Leather Interior", "Sport Package", "Heated Seats", "Navigation"],
        "image_url": "/static/images/BMW-rendering-front.jpg",
        "description": "Luxury BMW 3 Series with sport package and premium amenities."
    },
    {
        "id": 4,
        "make": "Mercedes-Benz",
        "model": "C-Class",
        "year": 2022,
        "price": 50000,
        "mileage": 10000,
        "color": "White",
        "fuel_type": "Gasoline",
        "transmission": "Automatic",
        "engine": "2.0L Turbo 4-Cylinder",
        "features": ["Premium Sound", "Leather Interior", "Sport Package", "Heated Seats", "Navigation"],
        "image_url": "/static/images/Mercedes-Benz-2024.jpg",
        "description": "Luxury Mercedes-Benz C-Class with sport package and premium amenities."
    },
    {
        "id": 5,
        "make": "Audi",
        "model": "A4",
        "year": 2023,
        "price": 40000,
        "mileage": 15000,
        "color": "Black",
        "fuel_type": "Gasoline",
        "transmission": "Automatic",
        "engine": "2.0L Turbo 4-Cylinder",
        "features": ["Premium Sound", "Leather Interior", "Sport Package", "Heated Seats", "Navigation"],
        "image_url": "/static/images/Audi-2024.jpg",
        "description": "Luxury Audi A4 with sport package and premium amenities."
    },
    {
        "id": 6,
        "make": "Tesla",
        "model": "Model 3",
        "year": 2024,
        "price": 50000,
        "mileage": 10000,
        "color": "White",
        "fuel_type": "Electric",
        "transmission": "Automatic",
        "engine": "Electric",
        "features": ["Autopilot", "Premium Sound", "Leather Interior", "Sport Package", "Heated Seats", "Navigation"],
        "image_url": "/static/images/Tesla-2024.jpg",
        "description": "Luxury Tesla Model 3 with autopilot and premium amenities."
    }
            ]

async def main():
    # clean + insert (safe for dev)
    await db.cars.delete_many({})
    await db.cars.insert_many(cars)
    count = await db.cars.count_documents({})
    print(f"✅ Seeded {count} cars")

if __name__ == "__main__":
    asyncio.run(main())
