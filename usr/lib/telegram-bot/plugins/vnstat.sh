#!/bin/sh

token=$(uci get telegram-bot.config.bot_token 2>/dev/nul)
chat_id=$(uci get telegram-bot.config.chat_id 2>/dev/nul)

if [ -z "$token" ]; then
	echo "token is empty"
	exit 2
fi

if [ -z "$chat_id" ]; then
	echo "chat_id is empty"
	exit 2
fi

vnstat -u
sleep 1
vnstati -s -o /tmp/vnstat_summary.jpg
vnstati -d -o /tmp/vnstat_daily.jpg
curl -o /dev/null -w "" -X POST https://api.telegram.org/bot${token}/sendMediaGroup \
-F chat_id=${chat_id} \
-F media='[
  {"type": "photo", "media": "attach://image1", "caption": "Summary"},
  {"type": "photo", "media": "attach://image2", "caption": "Daily"}
]' \
-F image1=@/tmp/vnstat_summary.jpg \
-F image2=@/tmp/vnstat_daily.jpg 2>/dev/null