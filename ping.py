import time
import subprocess
import os

hostname=raw_input('')
response = os.system("ping -c 1" + hostname)

if response ==0 :
	print 'server is down'
else :
	while 1:
			os.system("ping -c 10 -i 5 " + hostname + " >1.txt" )	
			os.system("awk -F'[= ]' '{print $6,$10}' < 1.txt >final.txt")			
			os.system("grep [0-9] final.txt >final1.txt")
			os.system("ping -c 720 -i 5" + hostname + ">2.txt")
			os.system("awk -F'[= ]' '{print $6,$10}' < 2.txt >final.txt")	
			os.system("grep [0-9] final.txt >final1.txt")
