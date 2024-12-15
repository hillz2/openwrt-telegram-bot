#!/bin/sh

docker logs --tail 5 cloudflared 2>&1 | sed 's/[^a-zA-Z0-9_ -]//g'
