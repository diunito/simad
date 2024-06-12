#!/bin/bash
check_web() {
	# $2: ip
	# $3: port
	curl http://$2:$3 --write-out "%{http_code}" --silent --output /dev/null
}
check_tcp() {
	# $2: ip
	# $3: port
	return nc -w 3 $2 $3
}
check_serv() {
	# $1: service type (web, tcp)
	# $2: ip
	# $3: port
	if [ "$1" = "web" ];then
		return check_web $2 $3
	elif [ "$1" = "tcp" ];then
		return check_tcp $2 $3
	fi
}

check_single_service() {
	serv_type="$1"
	ip="$2"
	port="$3"
	serv_name="$4"

	echo -n "testing type $serv_type\t$ip:$port ($serv_name)... " 
	if ! check_serv $serv_type $ip $port;then
		echo "FAILED"
	else
		echo "OK"
	fi
}
