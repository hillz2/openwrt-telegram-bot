#!/bin/sh

echo "FREE RAM"
cat /proc/meminfo | sed -n '1,5p'
echo ""
echo "FREE DISK SPACE"
df -h / /mnt/sda1 /mnt/sda3 /mnt/sda4 /mnt/sdb1
