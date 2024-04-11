#!/bin/bash

# get the tulip folder

echo " ________  ___  ___      ___ _______           _____ ______   _______           ________  ________  ________  ________  ________  ___  ___       "
echo "|\   ____\|\  \|\  \    /  /|\  ___ \         |\   _ \  _   \|\  ___ \         |\   __  \|\   ____\|\   __  \|\   __  \|\   ____\|\  \|\  \      "
echo "\ \  \___|\ \  \ \  \  /  / | \   __/|        \ \  \\\__\ \  \ \   __/|        \ \  \|\  \ \  \___|\ \  \|\  \ \  \|\  \ \  \___|\ \  \ \  \     "
echo " \ \  \  __\ \  \ \  \/  / / \ \  \_|/__       \ \  \\|__| \  \ \  \_|/__       \ \   ____\ \  \    \ \   __  \ \   ____\ \_____  \ \  \ \  \    "
echo "  \ \  \|\  \ \  \ \    / /   \ \  \_|\ \       \ \  \    \ \  \ \  \_|\ \       \ \  \___|\ \  \____\ \  \ \  \ \  \___|\|____|\  \ \__\ \__\   "
echo "   \ \_______\ \__\ \__/ /     \ \_______\       \ \__\    \ \__\ \_______\       \ \__\    \ \_______\ \__\ \__\ \__\     ____\_\  \|__|\|__|   "
echo "    \|_______|\|__|\|__|/       \|_______|        \|__|     \|__|\|_______|        \|__|     \|_______|\|__|\|__|\|__|    |\_________\  ___  ___ "
echo "                                                                                                                          \|_________| |\__\|\__\\"
echo "                                                                                                                                       \|__|\|__|"
echo "                                                                                                                                                 "
echo "Start downloading pcaps from the folder /tmp/pcaps/ on the vuln box"
if [$# -ne 3]
  then
    echo "No arguments supplied"
    echo "Usage: ./tulip_companion.sh <vuln_box_ip> <vuln_box_password> <tulip_pcap_folder_path>"
    exit 1
fi

ip=$1
PSWD=$2
path=$3

# evry 2 minutes download folder from vuln
while true
  do
    sshpass -p $PSWD rsync -vr root@$ip:/tmp/pcaps/\* $path
    # print info about the download
    sleep 120
  done
