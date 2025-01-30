#!/bin/sh

if [ -f /etc/init.d/cloudflared ]; then
        /etc/init.d/cloudflared restart
else
        echo "$(docker restart cloudflared) restarted"
fi
echo "To see the log file, type: /cloudflared_log"
