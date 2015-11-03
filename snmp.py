import time
import subprocess
import os

hostname=raw_input('')

for i in range(0,20):
        os.system("snmpget -v 1 -c public "+ hostname + " 1.3.6.1.2.1.2.2.1.10.1 >>2.txt")
        time.sleep(2)
os.system("awk -F'[: ]' '{print $7}' < 2.txt >final_last.txt")
os.system("awk 'NR>1{print $1-p} {p=$1}' final_last.txt >final_lat2.dat")

