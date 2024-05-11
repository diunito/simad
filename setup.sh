#!/bin/bash
#diff 2ndsimad/CApp/CApp/src/code/wm.py orig/CApp/CApp/src/code/wm.py # incompleta
#diff 2ndsimad/FIXME/fixme/src/api/products.js orig/FIXME/fixme/src/api/products.js # incompleta
#diff 2ndsimad/CC-Manager/app/crypto.py orig/CC-Manager/app/crypto.py # completa


#scp \
#	2ndsimad/CC-Manager/app/crypto.py \
#	2ndsimad/FIXME/fixme/src/api/products.js \
#	2ndsimad/CApp/CApp/src/code/wm.py \
#	root@10.60.81.1:/root
#
#vimdiff serv_orig/CApp/CApp/src/code/wm.py serv2/CApp/CApp/src/code/wm.py
#vimdiff serv_orig/CApp/.env serv2/CApp/.env
#vimdiff serv_orig/CC-Manager/app/crypto.py serv2/CC-Manager/app/crypto.py
#vimdiff serv_orig/CC-Manager/app/service.py serv2/CC-Manager/app/service.py
#vimdiff serv_orig/CC-Manager/app/users.py serv2/CC-Manager/app/users.py
#vimdiff serv_orig/CC-Manager/app/utils.py serv2/CC-Manager/app/utils.py
#vimdiff serv_orig/CC-Manager/docker-compose.yml serv2/CC-Manager/docker-compose.yml
#vimdiff serv_orig/FIXME/docker-compose.yml serv2/FIXME/docker-compose.yml
#vimdiff serv_orig/FIXME/fixme/src/api/products.js serv2/FIXME/fixme/src/api/products.js


set -x # to see executed commands
vm_ip="10.60.81.1"
ssh root@${vm_ip} 'git clone https://github.com/koraynilay/simad; cd simad; ./deploy.sh;'
scp serv2/CApp/CApp/src/code/wm.py        root@${vm_ip}:/root/CApp/CApp/src/code/wm_patched.py
scp serv2/CApp/.env                       root@${vm_ip}:/root/CApp/.env_patched
ssh root@${vm_ip} 'cd CApp/CApp/src/code; mv -v wm.py wm_orig.py; mv -v wm_patched.py wm.py;
			cd ~; cd CApp; mv -v .env .env_orig; mv -v .env_patched .env;
			cd ~; cd CApp; docker compose up --build --remove-orphans;'
scp serv2/CC-Manager/app/crypto.py        root@${vm_ip}:/root/CC-Manager/app/crypto_patched.py
ssh root@${vm_ip} 'cd CC-Manager/app; mv -v crypt.py crypto_orig.py; mv -v crypto_patched.py crypto.py;
			cd ~; cd CC-Manager; docker compose up --build --remove-orphans;'
scp serv2/FIXME/docker-compose.yml        root@${vm_ip}:/root/FIXME/docker-compose_patched.yml
scp serv2/FIXME/fixme/src/api/products.js root@${vm_ip}:/root/FIXME/fixme/src/api/products_patched.js
ssh root@${vm_ip} 'cd FIXME; mv -v docker-compose.yml docker-compose_orig.yml; mv -v docker-compose_patched.yml docker-compose.yml;
			cd ~; cd FIXME/fixme/src/api; mv -v products.js products_orig.js; mv -v products_patched.js products.js;
			cd ~; cd FIXME; docker compose up --build --remove-orphans;'

# TODO: give list of patched files and apply them automatically
