#! /usr/bin/python2

# Reformats and prints out the temperature of the cpu
import sys
import subprocess
import time


while True:
	raw_temp_str = subprocess.check_output("sensors", shell=True)
	# print "Raw Temp"
	startIndex = raw_temp_str.find('Core')
	temp = raw_temp_str[startIndex:]		
	
	startIndex = temp.find('Core')
	endIndex = temp.find(')') + 1

	temp = temp[startIndex:endIndex]
	
	# core0_temp = raw_temp_str[startIndex:endIndex]

	# print core0_temp
	print temp
	# print "startIndex:", temp.find('Core')
	# print "endIndex:", temp.find(')')
	time.sleep(1)