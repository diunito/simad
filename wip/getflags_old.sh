#!/bin/bash
[[ "$#" -lt 2 ]] \
	&& echo -e "Usage: $0 [service name] [script executable]" \
	&& echo "OR" \
	&& echo "Usage: $0 [service name] [script executable] [team ip]" \
	&& exit 1
team=$3
service=$1
dir="/tmp"
ip="10.10.0.1"
port="8081"
if [ "$#" -eq 2 ];then
	filename="${dir}/flagids_${service}.json"
	curl http://$ip:$port/flagIds\?service\=$service > "$filename"
elif [ "$#" -eq 3 ];then
	filename="${dir}/flagids_${service}_${team}.json"
	curl http://$ip:$port/flagIds\?service\=$service\&team\=$team > "$filename"
fi
./"$2" "$filename"
rm -v "$filename"
