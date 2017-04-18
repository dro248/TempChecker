#! /usr/bin/python2
import time
import subprocess
import json

while True:
    #raw_temp_str = subprocess.check_output("sensors", shell=True)
    raw = subprocess.check_output("sensors | grep 'CPU Temperature'", shell=True)
    temp = raw[21:].split()[0][:-3]
    high = raw[21:].split()[3][1:-1][:-3]
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    
    json_string = json.dumps({'datetime':datetime, 'temp':temp, 'high':high})
    #output = "datetime:", datetime, "|temp:", temp, "|high:", high

    # append to file
    f = open("temp.log", "a+")
    f.write(json_string + '\n')
    f.close()
    time.sleep(5)    
