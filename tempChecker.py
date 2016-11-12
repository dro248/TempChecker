#! /usr/bin/python2

# Reformats and prints out the temperature of the cpu
import sys
import subprocess
import time


while True:
	raw_temp_str = subprocess.check_output("sensors", shell=True)
	print "Raw Temp"
	print raw_temp_str
	time.sleep(1)