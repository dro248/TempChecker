import time
import subprocess

while True:
    #raw_temp_str = subprocess.check_output("sensors", shell=True)
    raw_temp_str = subprocess.check_output("sensors | grep temp", shell=True)
    print raw_temp_str
    #f = open("temp.log", "w+")
    time.sleep(1)    
