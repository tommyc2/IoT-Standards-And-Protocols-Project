from pymongo.mongo_client import MongoClient

password = "pw"
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


def save_to_database(temp,pressure,direction,humidity,location):
    data = {
    "temp": temp, 
    "pressure": pressure,
    "humidity": humidity,
    "direction": direction,
    "location": location,
    }

    collection.insert_one(data)


def save_distance(distance):
    collection.insert_one({"distance": int(distance) })


#################
# Avg temperature
##################


def get_average_temp():
    average_temp = collection.aggregate([
  {
        "$group": {
            "_id": None,
            "avgTemp": {"$avg": "$temp"}
        }
    }
])
    for output in average_temp:
        return output["avgTemp"]



#################
# Avg pressure
##################

def get_avg_pressure():
    average_pressure = collection.aggregate([
  {
        "$group": {
            "_id": None,
            "avgPressure": {"$avg": "$pressure"}
        }
    }
])
    for output in average_pressure:
        return output["avgPressure"]




#################
# Avg humidity
##################

def get_avg_humidity():
    average_hum = collection.aggregate([
  {
        "$group": {
            "_id": None,
            "avgHumidity": {"$avg": "$humidity"}
        }
    }
])
    for output in average_hum:
        return output["avgHumidity"]


#################
# Total distance
##################


def get_total_distance():
    total = collection.aggregate([
  {
        "$group": {
            "_id": None,
            "totalDistance": {"$sum": "$distance"}
        }
    }
])
    for i in total:
        return i["totalDistance"]


print(get_total_distance())


    




