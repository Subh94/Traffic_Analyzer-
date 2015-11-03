import time
import subprocess
import os

hostname=raw_input('')

#while 1:
os.system("ping -c 10 -i 5 " + hostname + " >1.txt")
os.system("awk -F'[= ]' '{print $6,$10}' < 1.txt >final.txt")
os.system("grep [0-9] final.txt >final1.txt")
os.system("grep -v [0-9] final1.txt > temp.txt && mov temp.txt >final1.txt")
