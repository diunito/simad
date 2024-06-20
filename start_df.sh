#!/bin/bash
set -a # set allexport so that the sourced .env vars are exported
. priv/DestructiveFarm/.env
DestructiveFarm/server/start_server.sh
set +a # unset allexport
