#!/bin/bash

# check sudo
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo " ________  ________  ________  ________  ________           ________  ___  ___  _____ ______   ________  _______   ________     "
echo "|\   __  \|\   ____\|\   __  \|\   __  \|\   ____\         |\   ___ \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    "
echo "\ \  \|\  \ \  \___|\ \  \|\  \ \  \|\  \ \  \___|_        \ \  \_|\ \ \  \\\  \ \  \\\__\ \  \ \  \|\  \ \   __/|\ \  \|\  \   "
echo " \ \   ____\ \  \    \ \   __  \ \   ____\ \_____  \        \ \  \ \\ \ \  \\\  \ \  \\|__| \  \ \   ____\ \  \_|/_\ \   _  _\  "
echo "  \ \  \___|\ \  \____\ \  \ \  \ \  \___|\|____|\  \        \ \  \_\\ \ \  \\\  \ \  \    \ \  \ \  \___|\ \  \_|\ \ \  \\  \| "
echo "   \ \__\    \ \_______\ \__\ \__\ \__\     ____\_\  \        \ \_______\ \_______\ \__\    \ \__\ \__\    \ \_______\ \__\\ _\ "
echo "    \|__|     \|_______|\|__|\|__|\|__|    |\_________\        \|_______|\|_______|\|__|     \|__|\|__|     \|_______|\|__|\|__|"
echo "                                           \|_________|                                                                         "
echo "                                                                                                                                "
echo "                                                                                                                                "


# check --help
if [ "$1" == "--help" ]; then
  echo "Tool to automate the execution of tcpdump and optionally send them to a tulip server"
  echo "Usage: ./dump.sh <dir>  -- For execute only the tcpdump"
  echo "Usage: ./dump.sh <dir> <tulip_ip> <tulip_password> -- For execute the tcpdump and send the pcap to the tulip server"
  echo "PS: recommended folder: /tmp/pcaps/" 
  exit 1
fi


interrupt_handler() {
    echo "Interruzione ricevuta. Terminazione in corso..."
    # Puoi aggiungere eventuali azioni di pulizia o altre operazioni qui, se necessario.
    # Ad esempio, puoi terminare il processo tcpdump usando il suo PID (se disponibile).
    if [[ -n $tcpdump_pid ]]; then
        kill $tcpdump_pid
    fi
    exit 1
}

trap interrupt_handler SIGINT

# check args < 1
if [ $# -lt 1 ]
  then
    echo "No arguments supplied"
    echo "Usage: ./dump.sh <dir>" 
    echo "or"
    echo "Usage: ./dump.sh <dir> <tulip_ip> <tulip_password>"
    exit
fi

dir=$1

if [ $# -eq 3 ]
  then
    ip=$2
    pass=$3
fi

# check if dir exist
if [ ! -d "$dir" ] 
  then
    echo "Folder $dir does not exist, creating it"
    mkdir $1
fi

touch "$dir/eve.json"

i=1
j=1
# check if exist files on format CTF_dump_*.pcap
if [ "$(ls -A $dir) | grep CTF_dump" ]
  then
    i=$(ls -A $dir | grep CTF_dump | tail -n 1 | cut -d'_' -f3 | cut -d'.' -f1)
    echo "Last dump file: $i"
    i=$((i+1))
    echo "Continue from $i"
fi

# start dump and upload 
while true
do
    echo "Dumping $i"
    timeout 120 tcpdump -i game -w ${dir}/CTF_dump_$i.pcap port not 22 &
    tcpdump_pid=$!
    wait $tcpdump_pid
    if [ $# -eq 3 ]
      then
        echo "Uploading $i"
        curl -F "file=@${dir}CTF_final_$i.pcap" http://$ip:5000/upload -u "tulip:$pass"
    fi
    i=$((i+1))
    sleep 2
done
