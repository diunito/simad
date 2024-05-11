#!/bin/bash
handle_exit() {
	echo 'got Ctrl+C, killing all sploits'
	for pid in $@;do
		kill -INT $pid
		echo "killed $pid"
	done
}

single=${1:-no}
startf="$PWD"
ssf="$startf" # start_sploit.py folder
curf="$1"
ip="10.81.81.16"
port="5000"
tokfile="/tmp/.dftok"
if ! [ -f "$tokfile" ];then
	echo "Error: no tokfile, do 'echo [your-df-api-token] > $tokfile'"
	exit 1
fi

if [ "$curf" = "--help" ];then
	echo "Usage: $0 [folder with only sploits]"
	exit 0
fi

if ! [ -d "$curf" ];then
	echo "Usage: $0 [folder with only sploits]"
	exit 2
fi
cd "$curf"

pids=()
for script in *;do
	if [ "$script" = "start_sploit.py" ] || [ "$script" = "start_sploits.sh" ];then
		continue
	fi
	script="$PWD/$script"
	if [ "$single" = "yes" ];then
		echo "$ssf"/start_sploit.py "$script" -u "$ip:$port" --token "$(<$tokfile)"
	else
		"$ssf"/start_sploit.py "$script" -u "$ip:$port" --token "$(<$tokfile)" &
		pids+=("$!")
	fi
done

if ! [ "$single" = "yes" ];then
	echo sploits pids: ${pids[*]}
	trap "handle_exit ${pids[*]}" SIGINT
	echo trapped

	for pid in ${pids[*]};do
		wait $pid
	done
fi
