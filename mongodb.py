from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

MONGODB_ATLAS_URI = os.getenv("MONGODB_ATLAS_URI_actions")
client = MongoClient(MONGODB_ATLAS_URI)
db = client.get_database()

def get_actions_collection():
    return db['actions']
list_of_actions = []
try:
    actions = get_actions_collection()
    print("Count:", actions.count_documents({}))
    print("MongoDB connection OK")
    
    print("\n--- All Documents ---")
    for d in actions.find():
        list_of_actions.append(d)
    
except Exception as e:
    print("Error:", e)
