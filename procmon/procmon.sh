#!/bin/bash

cd $PROCMON_HOME/lib
while true;
do
	clear
	python LinuxShellMonitoring.py
	read -n 1 -t 5 input
	if [ $input == "q" ];
	then
		exit;
	fi
done
