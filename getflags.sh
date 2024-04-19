#!/bin/bash
[[ "$#" -ne 2 ]] && echo -e 'Usage: $0 [service name] [script executable]' && exit 1
service=$1
filename="flagids_$service.json"
#curl http://10.10.0.1:8081/flagIds\?service\=$service | jq > "$filename"
curl http://10.10.0.1:8081/flagIds\?service\=$service > "$filename"
./"$2" "$filename"
