# test_mongo.py
import asyncio
from database import db

async def main():
    print(await db.command("ping"))
    print("Cars count:", await db.cars.count_documents({}))

asyncio.run(main())
