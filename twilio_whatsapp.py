import datetime
from pymongo.mongo_client import MongoClient
from twilio.rest import Client

account_sid = 'key'
auth_token = 'key'
client = Client(account_sid, auth_token)

dummy_float = 24.5
dummy_string = "Waterford"
sender_number = "+14155238886"
receiver_number = "+353874495213"

message = client.messages.create(
  from_ = f'whatsapp:{sender_number}',
  body = f'Avg Temp: {dummy_float} degrees (C), Avg Place: {dummy_string}', 
  to = f'whatsapp:{receiver_number}'
)

print(message.sid)
