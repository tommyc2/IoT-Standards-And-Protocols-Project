import datetime
from pymongo.mongo_client import MongoClient

password = "PASSWORD_GOES_HERE"
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

data = [{
    "xaxis": 10,
    "yaxis": 20
},
{
    "xaxis": 20,
    "yaxis": 40
},
{
    "xaxis": 30,
    "yaxis": 60
}
]

collection.insert_many(data)

    




