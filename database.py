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

data = [
    {
    "temp": 22.5, # Dummy values
    "lat": 0, # Dummy values
    "long": 0, # Dummy values
    "pressure": 1020
    },
    {
    "temp": 24.5, # Dummy values
    "lat": 0, # Dummy values
    "long": 0, # Dummy values
    "pressure": 1050
    },
    {
    "temp": 23.5, # Dummy values
    "lat": 0, # Dummy values
    "long": 0, # Dummy values
    "pressure": 600
    }
]

# 15 rows already inserted --> collection.insert_many(data)

average_temp = db.collection.aggregate([
    {
        "$group": {
            "_id": None,
            "avgTemp": {"$avg": "$temp"}
        }
    }
])

for i in average_temp:
    print(i["avgTemp"])






    




