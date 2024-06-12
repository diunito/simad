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
	# $1: type (web, tcp)
	# $2: ip
	# $3: port
	if [ "$1" = "web" ];then
		return check_web $2 $3
	elif [ "$1" = "tcp" ];then
		return check_tcp $2 $3
	fi
}

echo -n "testing type $type\t$ip:$port ($serv)... " 
if ! check_serv $type $ip $port;then
	echo "FAILED"
else
	echo "OK"
fi

#delis() {
#}
#
#while read a; do 
#	la="$(echo $a | cut -f2 -d' ')"
#	msid="$(echo $a | cut -f1 -d' ')"
#	echo $la $msid
#	ret="$(delis $la $msid)";
#	echo $ret
#	while [ $ret == "429" ];do
#		sleep 5;
#		ret="$(delis $la $msid)";
#		echo while: $ret
#	done
#	sleep 0.2;
#done < abcd_la


# jq '.[] | select(.track_metadata.additional_info.media_player == "org.kde.kdeconnect_tp") | "\(.recording_msid) \(.listened_at)"' listens.json | tr -d '"' >> abcd_la
# listens.json is the downloaded json from listenbrainz
# https://zerokspot.com/weblog/2013/07/18/processing-json-with-jq/
# https://stackoverflow.com/a/18608100
# .env is just the token taken from https://listenbrainz.org/profile
