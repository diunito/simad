#!/bin/bash
. $HOME/simad/ctf_scripts/lib/servinfo/serv_status.sh
. $HOME/simad/ctf_scripts/lib/misc.sh
json=$(<$HOME/services.json)

ip=10.60.81.1
jq -c '.[]' <<< $json | while read serv; do
	servname=$(get_json_value "name" "$serv")
	jq -c '.containers[]' <<< $serv | while read containers; do
		servtype=$(get_json_value "type" "$containers")
		port=$(get_json_value "listen_port" "$containers")
		echo "$serv_type $ip $port $serv_name $container_name... "
	done
done
