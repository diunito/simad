#!/bin/bash
check_web() {
	# $2: ip
	# $3: port
	curl http://$2:$3 --write-out "%{http_code}" --silent --output /dev/null
	local ret=$?
	echo -n " $ret "
	if [ "$ret" = "200" ];then
		return 0
	else
		return 1
	fi
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
	local serv_type="$1"
	local ip="$2"
	local port="$3"
	local serv_name="$4"
	local container_name="$4"

	# example output:
	# testing type web 10.60.81.1:80 fimlibrary (nginx)... OK
	# testing type tcp 10.60.81.1:1337 rpn (rpn)... FAILED
	# testing type sql 10.60.81.1:3306 filmlibrary (filmlibrary_sql)... FAILED
	echo -en "testing type $serv_type\t$ip:$port $serv_name ($container_name)... "
	if ! check_serv $serv_type $ip $port;then
		echo "FAILED"
	else
		echo "OK"
	fi
}
