#!/bin/bash
simad_folder="$HOME/simad"
servs_backup_folder="/servs"

# backup everything
cp -avr "$HOME" "$servs_backup_folder"

# install and start firegex
"$simad_folder/start_firegex.sh"

# start tcpdump
"$simad_folder"/ctf_scripts/vuln/dump.sh /pcaps
