#!/bin/sh
simad_folder="$HOME/simad"

# clone simad repo in $HOME (should be /root)
git clone --recurse-submodules https://github.com/koraynilay/simad "$simad_folder"

cd "$simad_folder" || echo "cd $simad_folder failed" && return
./deploy.sh "$@"
