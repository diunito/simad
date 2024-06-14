#!/bin/false
# $1: key, $2: json object
get_json_value() {
	local ret="$(jq ".[\"$1\"]  // empty" <<< "$2")"
	ret=${ret#\"}
	ret=${ret%\"}
	printf '%s' "$ret"
}

