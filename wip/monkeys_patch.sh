#!/bin/bash
servs_json=$(python -c 'import json;import tulip.services.configurations as s; print(json.dumps(s.services))' | jq '.[].name')
echo $servs_json
