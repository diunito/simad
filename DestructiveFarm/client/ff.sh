#!/bin/bash
mysql -h $1 --port 3306 --user=filmlibrary --password='Str0ng_P4szw0rd!' -e 'use filmlibrary;select description from films where description like "ptm%";' | tr -d '|'
