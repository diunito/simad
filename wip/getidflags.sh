#!/bin/bash
[[ "$#" -lt 2 ]] \
	&& echo "Usage: $0 [service name] [team ip]" \
	&& exit 1

if [ "$3" = "-d" ];then
	set -x
fi
service="$1"
team="$2"

ip="${IDFIP:-10.10.0.1}"
port="${IDFPORT:-8081}"

curl http://$ip:$port/flagIds\?service\=$service\&team\=$team

if [ "$3" = "-d" ];then
	set +x
fi
