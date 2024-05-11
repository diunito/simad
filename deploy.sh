#!/bin/sh
simad_folder="$HOME/simad"

# install and start firegex
if [ -n "$1" ];then
	"$simad_folder"/firegex.py --port 65000 --startup-psw "$1"
else
	"$simad_folder"/firegex.py --port 65000
fi
# uncomment this if you want to get the latest version
#sh <(curl -sLf https://pwnzer0tt1.it/firegex.sh) --port 65000

# start tcpdump
"$simad_folder"/ctf_scripts/vuln/dump.sh /pcaps
