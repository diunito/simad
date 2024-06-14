#!/bin/false
import os
import requests

def getidflags(serv, team, dry=False):
    # for ip and port set 'SYSTEM_ID_FLAGS_IP' and 'SYSTEM_ID_FLAGS_PORT' in DestructiveFarm's config.py
    # they will be set automatically by (our) start_sploit.py
    # set them manually (or use the default values) for use not with (our) DestructiveFarm
    ip = os.getenv("IDFIP", "10.10.0.1")
    port = os.getenv("IDFPORT", "8081")

    # no yellow highlighting because python sucks more than twin-turbo (and import termcolor may not work)
    if os.getenv("IDFIP") is None:
        print(f"WARN: $IDFIP not set, using default {ip}")
    if os.getenv("IDFPORT") is None:
        print(f"WARN: $IDFPORT not set, using default {port}")

    url = f"http://{ip}:{port}/flagIds?service={serv}&team={team}"
    if dry:
        print(url)
    else:
        response = requests.get(url)
        # returns a dictionary
        return response.json()[serv][team]
