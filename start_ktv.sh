#!/bin/bash

cd ~/kaos_tv/

pwd
echo "User: $USER"
echo "enter conda env"miniconda3/envs/kaos_tv/bin/python kaos_tv/main.py
cdate=$(date)
echo "date $cdate"

ret=$(conda --version)
echo "ret: $ret"

echo "activate"
ret=$(conda activate kaos_tv)
echo "ret: $ret"

echo "start KAOS TV"
#python play_media.py
#python telegram_bot.pyi
cmd="python test.py"
ret=$($cmd)
echo "ret: $ret"

i=0
while true
do
	echo "piep $i"
	sleep 10
	i=$i+1
done
