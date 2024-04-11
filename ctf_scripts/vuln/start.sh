#!/bin/bash 

# check sudo 
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo " ________               _______            _____              ________  ________  ___  ___       ";
echo "|\_____  \             /  ___  \          / __  \            |\   ____\|\   __  \|\  \|\  \      ";
echo "\|____|\ /_           /__/|_/  /|        |\/_|\  \           \ \  \___|\ \  \|\  \ \  \ \  \     ";
echo "      \|\  \          |__|//  / /        \|/ \ \  \           \ \  \  __\ \  \\\  \ \  \ \  \    ";
echo "     __\_\  \ ___ ___ ___ /  /_/__  ___ ___ __\ \  \ ___ ___ __\ \  \|\  \ \  \\\  \ \__\ \__\   ";
echo "    |\_______\\__\\__\\__\\________\\__\\__\\__\ \__\\__\\__\\__\ \_______\ \_______\|__|\|__|   ";
echo "    \|_______\|__\|__\|__|\|_______\|__\|__\|__|\|__\|__\|__\|__|\|_______|\|_______|   ___  ___ ";
echo "                                                                                       |\__\|\__\\";
echo "                                                                                       \|__|\|__|";
echo "                                                                                                 ";

echo "BackUP services"
cp -r . ./old

# install python3, pip and tmux
echo "Installing python3, pip and tmux"
apt install python3 tmux python3-pip -y
# pacman -S python3 tmux --noconfirm
# dnf install -y python3 tmux 

# install python packages
echo "Installing python packages"
pip3 install requests 
pip3 install docker
pip3 install json

echo "Downloading the proxy"
git clone https://github.com/ByteLeMani/ctf_proxy

# download pcap dumper
echo "Download pcap Dumper"
wget https://raw.githubusercontent.com/AlessandroMIlani/ctf_scripts/main/vuln/dump.sh
chmod +x dump.sh

echo "Download the proxy helper"
wget https://raw.githubusercontent.com/AlessandroMIlani/ctf_scripts/main/vuln/proxy_helper.py
python3 proxy_helper.py


