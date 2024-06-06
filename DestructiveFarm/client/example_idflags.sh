#!/bin/bash
# forse un giorno la farò anche come libreria, ma non serve a molto
#$libdir='../../ctf_scripts/exploits_lib')
#. $libdir/getidflags.sh
#
#getidflags
echo s$1s
j=$(../../ctf_scripts/exploits_lib/getidflags.sh 'CCap' '1' -n)
#j=$(jq <<< "$j") # commented because it's in dry mode, so obviously it won't be a valid json
echo $j
