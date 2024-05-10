#!/bin/bash
handle_exit() {
	for pid in $@;do
		pkill --signal SIGINT -P $pid
		kill $pid
		echo "killed $pid and children (hopefully)"
	done
}

single=${1:-no}
startf="$PWD"
ssf="$startf" # start_sploit.py folder
logf="logs"
curf="cur"
ip="10.81.81.16"
port="5000"
tokfile="/tmp/.dftok"
if ! [ -f "$tokfile" ];then
	echo "Error: no tokfile, do 'echo [your-df-api-token] > $tokfile'"
	exit 1
fi

if ! [ -d "$curf" ];then
	echo "Error: no '$curf' folder"
	exit 2
fi
cd "$curf"

if ! [ -d "$logf" ];then
	mkdir -v "$logf"
fi

pids=()
for script in *;do
	la="$logf/$script.log"
	script="$PWD/$script"
	if [ "$single" = "yes" ];then
		echo "$ssf"/start_sploit.py "$script" -u "$ip:$port" --token "$(<$tokfile)"
	else
		"$ssf"/start_sploit.py "$script" -u "$ip:$port" --token "$(<$tokfile)" 2>&1 3>&1 1> "$la" &
		pids+=("$!")
	fi
done

if ! [ "$single" = "yes" ];then
	echo ${pids[*]}
	trap "handle_exit ${pids[*]}" SIGINT
	echo trapped

	sleep 0.5
	cd "$logf"
	tail -f *.log
fi
