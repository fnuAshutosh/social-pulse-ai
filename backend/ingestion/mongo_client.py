#backend/ingestion/mongo_client.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
print(f"Mongo URI: {MONGO_URI}")
if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set.")
client = MongoClient(MONGO_URI)
db = client['social-pulse']
collection = db['posts']