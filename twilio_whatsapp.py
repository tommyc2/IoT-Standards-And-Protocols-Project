import datetime
from pymongo.mongo_client import MongoClient
from twilio.rest import Client
import database

account_sid = 'sid'
auth_token = 'token'
client = Client(account_sid, auth_token)

sender_number = "send_num"
receiver_number = "my_num"
humidity = database.get_avg_humidity()

if (database.get_avg_humidity()==None):
    humidity = 0

message = client.messages.create(
  from_ = f'whatsapp:{sender_number}',
  body = f'Your vehicle report: Avg Temp: {round(database.get_average_temp(),2)} degrees (C), Avg Humidity: {round(humidity,2)}, Avg Pressure: {round(database.get_avg_pressure(),2)}, Total Distance this week: {database.get_total_distance()} km',
  to = f'whatsapp:{receiver_number}'
)

print(message.sid)
