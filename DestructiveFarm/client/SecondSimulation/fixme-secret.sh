#!/bin/bash
curl http://"$1":8080/api/products | jq -r '.[].secret'
