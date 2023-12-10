#! /bin/bash

today=$(date +%Y%m%d)
weather_report=raw_data_$today
city=Casablanca

curl wttr.in/$city --output $weather_report
grep °C $weather_report > temperatures.txt

obs_tmp=$(cat -A temperatures.txt | head -1 | cut -d"+" -f2 | cut -d"^" -f1)
echo "observed temperature = $obs_tmp"

fc_tmp=$(sed -n '2p' temperatures.txt | cat -A| cut -d"+" -f3 | cut -d "^" -f1)
echo "forcasted temperature = $fc_tmp"

TZ='Morocco/Casablanca'
hour=$(TZ='Morocco/Casablanca' date -u +%H) 
day=$(TZ='Morocco/Casablanca' date -u +%d) 
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)


record=$(echo -e "$year\t$month\t$day\t$obs_tmp\t$fc_tmp")
echo $record >> rx_proc.log
