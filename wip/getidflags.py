#!/bin/python
import os

def getidflags(serv, team, ):
    ip = os.getenv("IDFIP", "10.10.0.1")
    port = os.getenv("IDFPORT", "8081")
    response = requests.get(f"http://{ip}:{port}/flagIds?service={serv}&team={team}")
    return response.json()[serv][team]
