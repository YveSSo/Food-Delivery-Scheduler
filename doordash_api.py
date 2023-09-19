from os import access
import jwt.utils
import time
import math
import requests
import uuid
import os
import json 
from dotenv import load_dotenv

load_dotenv()

DEVELOPER_ID = os.getenv("DEVELOPER_ID")
KEY_ID = os.getenv("KEY_ID")
SIGNING_SECRET = os.getenv("SIGNING_SECRET")

endpoint = "https://openapi.doordash.com/drive/v2/deliveries/"


def generate_door_dash_token(): 
    accessKey = {
        "developer_id": DEVELOPER_ID, #TODO: Update value with Developer ID
        "key_id": KEY_ID, #TODO: Update value with Key ID
        "signing_secret":SIGNING_SECRET #TODO: Update value with Signing Secret
    }

    token = jwt.encode(
    {
        "aud": "doordash",
        "iss": accessKey["developer_id"],
        "kid": accessKey["key_id"],
        "exp": str(math.floor(time.time() + 300)),
        "iat": str(math.floor(time.time())),
    },
    jwt.utils.base64url_decode(accessKey["signing_secret"]),
    algorithm="HS256",
    headers={"dd-ver": "DD-JWT-V1"})

    return token 

def create_delivery_request(): 
    delivery_id = str(uuid.uuid4()) #TODO: Replace with generated system ID

    headers = {"Accept-Encoding": "application/json",
             "Authorization": "Bearer " + generate_door_dash_token(),
            "Content-Type": "application/json"}


    request_body = { # Modify pickup and drop off addresses below
        "external_delivery_id": delivery_id,
        "pickup_address": "901 Market Street 6th Floor San Francisco, CA 94103",
        "pickup_business_name": "Wells Fargo SF Downtown",
        "pickup_phone_number": "+16505555555",
        "pickup_instructions": "Enter gate code 1234 on the callbox.",
        "dropoff_address": "901 Market Street 6th Floor San Francisco, CA 94103",
        "dropoff_business_name": "Wells Fargo SF Downtown",
        "dropoff_phone_number": "+16505555555",
        "dropoff_instructions": "Enter gate code 1234 on the callbox.",
        "order_value": 1999
    }

    create_delivery = requests.post(endpoint, headers=headers, json=request_body) # Create POST request

    return create_delivery

def get_delivery_request(): 
    headers = {"Accept-Encoding": "application/json",
            "Authorization": "Bearer " + generate_door_dash_token(),
            "Content-Type": "application/json"}

    get_delivery = requests.get(endpoint + '5ec0c066-41d2-45fc-bcc3-322261e33dea', headers=headers) # Create GET request

    return get_delivery
