# database.py
import os
from urllib.parse import quote_plus
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("MONGO_USER")
PASS = quote_plus(os.getenv("MONGO_PASS"))  # <-- encodes special characters
HOST = os.getenv("MONGO_HOST")
DB   = os.getenv("DB_NAME", "car_dealer")

if not USER or not PASS or not HOST:
    raise RuntimeError("❌ Missing MONGO_USER / MONGO_PASS / MONGO_HOST in .env")

MONGO_URI = (
    f"mongodb+srv://{USER}:{PASS}@{HOST}/"
    "?retryWrites=true&w=majority&authSource=admin"
)

client = AsyncIOMotorClient(MONGO_URI, tls=True)
db = client[DB]

async def init_db():
    # Test authentication
    try:
        await db.command("ping")
        print("✅ Connected to MongoDB Atlas")
    except Exception as e:
        print(f"❌ Could not connect to MongoDB: {e}")

    # Ensure numeric ID uniqueness
    await db.cars.create_index("id", unique=True)
