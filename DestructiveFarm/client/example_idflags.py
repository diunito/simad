#!/bin/python
import sys

sys.path.append('../../ctf_scripts/exploits_lib')
from getidflags import *

getidflags('CCap', '10.10.69.1', dry=True)
print(getidflags, flush=True)
