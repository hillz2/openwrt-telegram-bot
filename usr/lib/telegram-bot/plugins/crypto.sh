#!/bin/sh

if [[ ! -z $1 ]]; then
	crypto.py -b "$1" | sed 's/\[1m//g;s/\[0m//g'
else
	echo "Usage: /crypto [btc_value_in_usd]"
fi
