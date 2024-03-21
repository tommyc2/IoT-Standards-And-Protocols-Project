import datetime
from pymongo.mongo_client import MongoClient

password = "dungarvan1995"
uri = f"mongodb+srv://tcmedion:{password}@mycluster.m9wolg3.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"

client = MongoClient(uri)

db = client.get_database("IoTProtocolsDB")
collection = db.get_collection("Data")

def find_database():
    if (db != None):
        print(f"""
              Found database: {db.name}\n
              Found {collection.count_documents} collections
              """)
        return db

data = {
    "temp": 22.5, # Dummy values
    "lat": 0, # Dummy values
    "long": 0 # Dummy values
}

collection.insert(data)

    




