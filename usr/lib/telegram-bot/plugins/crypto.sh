#!/bin/sh

if [[ ! -z $1 ]]; then
	crypto.py -b "$1" | sed 's/\[1m//g;s/\[0m//g'
else
	crypto.py -b 400000 | sed 's/\[1m//g;s/\[0m//g'
	echo "=========="
	echo "Usage: /crypto [btc_value_in_usd]"
fi
