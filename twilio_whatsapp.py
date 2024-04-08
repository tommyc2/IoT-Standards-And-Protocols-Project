import datetime
from pymongo.mongo_client import MongoClient
from twilio.rest import Client
import database

account_sid = 'sid'
auth_token = 'auth'
client = Client(account_sid, auth_token)

dummy_string = "Waterford"
sender_number = "+14155238886"
receiver_number = "+353874495213"

message = client.messages.create(
  from_ = f'whatsapp:{sender_number}',
  body = f'Your vehicle report: Avg Temp: {database.get_average_temp()} degrees (C),
           Avg Humidity: {database.get_avg_humidity()},
           Avg Pressure: {database.get_avg_pressure()}',
  to = f'whatsapp:{receiver_number}'
)

print(message.sid)
