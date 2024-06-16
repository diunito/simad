#!/bin/bash
set -x # to see executed commands
vm_ip=""
vmpass=""
sshpass -p "$vmpass" ssh root@${vm_ip} 'git clone https://github.com/koraynilay/simad; cd simad; ./deploy.sh SaccintoSvizzera35;'
sshpass -p "$vmpass" scp serv2/CApp/CApp/src/code/wm.py        root@${vm_ip}:/root/CApp/CApp/src/code/wm_patched.py
sshpass -p "$vmpass" ssh root@${vm_ip} 'cd CApp/CApp/src/code; mv -v wm.py wm_orig.py; mv -v wm_patched.py wm.py;
 					cd ~; cd CApp; mv -v .env .env_orig;
		 			cd ~; cd CApp; ./deploy.sh;'
sshpass -p "$vmpass" scp serv2/CC-Manager/app/crypto.py        root@${vm_ip}:/root/CC-Manager/app/crypto_patched.py
sshpass -p "$vmpass" ssh root@${vm_ip} 'cd CC-Manager/app; mv -v crypto.py crypto_orig.py; mv -v crypto_patched.py crypto.py;
		 			cd ~; cd CC-Manager; docker compose up --build --remove-orphans -d;'
sshpass -p "$vmpass" scp serv2/FIXME/docker-compose.yml        root@${vm_ip}:/root/FIXME/docker-compose_patched.yml
sshpass -p "$vmpass" scp serv2/FIXME/fixme/src/api/products.js root@${vm_ip}:/root/FIXME/fixme/src/api/products_patched.js
sshpass -p "$vmpass" ssh root@${vm_ip} 'cd FIXME; mv -v docker-compose.yml docker-compose_orig.yml; mv -v docker-compose_patched.yml docker-compose.yml;
					cd ~; cd FIXME/fixme/src/api; mv -v products.js products_orig.js; mv -v products_patched.js products.js;
					cd ~; cd FIXME; docker compose up --build --remove-orphans -d;'

# TODO: give list of patched files and apply them automatically
