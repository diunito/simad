#!/bin/sh
#!/bin/bash
set -a # set allexport so that the sourced .env vars are exported
. priv/tulip/.env
cd tulip
docker compose up --build
