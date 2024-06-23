#!/bin/bash
set -a # set allexport so that the sourced .env vars are exported
. priv/firegex/.env

firegex/start.py --port "$FIREGEX_PORT" --psw-no-interactive "$FIREGEX_PSWD"
# use this instead if you want to get the upstream version
#sh <(curl -sLf https://pwnzer0tt1.it/firegex.sh) --port "$FIREGEX_PORT" $(if [ -n "$1" ];then echo --psw-no-interactive "$FIREGEX_PSWD";fi)

set +a # unset allexport
