#!/bin/sh

if [ -f /etc/init.d/cloudflared ]; then
        tail -n 10 /var/log/cloudflared.err | sed 's/[^a-zA-Z0-9_ -]//g'
else
        docker logs --tail 5 cloudflared 2>&1 | sed 's/[^a-zA-Z0-9_ -]//g'
fi
