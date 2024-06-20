#!/bin/bash
simad_folder="$HOME/simad"
servs_backup_folder="/servs"

# backup everything
cp -avr "$HOME" "$servs_backup_folder"

# install and start firegex
"$simad_folder/firegex/start.py" --port 65000 $(if [ -n "$1" ];then echo --psw-no-interactive "$1";fi)
# use this instead if you want to get the upstream version
#sh <(curl -sLf https://pwnzer0tt1.it/firegex.sh) --port 65000 $(if [ -n "$1" ];then echo --psw-no-interactive "$1";fi)

# start tcpdump
"$simad_folder"/ctf_scripts/vuln/dump.sh /pcaps
