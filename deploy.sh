#!/bin/sh
simad_folder="$HOME/simad"

# install and start firegex
sh <(curl -sLf https://pwnzer0tt1.it/firegex.sh)

# clone simad repo in $HOME (should be /root)
git clone --recurse-submodules https://github.com/koraynilay/simad "$simad_folder"

# start tcpdump
"$simad_folder"/ctf_scripts/vuln/dump.sh /pcaps
