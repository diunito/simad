#!/bin/sh
simad_folder="$HOME/simad"

# clone simad repo in $HOME (should be /root)
git clone --recurse-submodules git@github.com:diunito/simad "$simad_folder"

cd "$simad_folder" || echo "cd $simad_folder failed" && exit
./deploy.sh "$@"
