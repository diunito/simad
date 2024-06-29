#!/bin/bash
simad_folder="$HOME/simad"
servs_backup_folder="/servs"

# backup everything
cp -anvr "$HOME" "$servs_backup_folder"

# install and start firegex
"$simad_folder/start_firegex.sh"

# start tcpdump
tmux new-session -d -s tcpdump "$simad_folder"/start_tcpdump.sh

# start ctf_proxy
#"$simad_folder"/start_ctfproxy.sh
