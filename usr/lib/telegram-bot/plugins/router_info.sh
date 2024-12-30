#!/bin/bash

model=$(cat /tmp/sysinfo/model | sed $'s/[^[:print:]\t]//g')
free_ram=$(echo "$(free | grep Mem | awk '{print $7 / 1024}')" MB)
cpu_temperature=$(cat /sys/class/thermal/thermal_zone0/temp)
cpu_temperature=$(echo "$(($cpu_temperature/1000)) C")
available_space_root=$(df -h / | awk 'NR==2 {print $4}')
available_space_sda3=$(df -h /dev/sda3 | awk 'NR==2 {print $4}')
available_space_sdb1=$(df -h /dev/sdb1 | awk 'NR==2 {print $4}')

echo "• MODEL: $model"
echo "• FREE_RAM: $free_ram"
echo "• CPU_TEMPERATURE: $cpu_temperature"
echo "• UPTIME: $(uptime)"
echo "• ROOT (/): $available_space_root available"
echo "• MEDIA (/dev/sda3): $available_space_sda3 available"
echo "• SD_CARD (/dev/sdb1): $available_space_sdb1 available"
