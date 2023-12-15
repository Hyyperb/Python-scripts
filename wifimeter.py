import os
import time

def wifimeter(): # returns signal strength betw 0-100
	return os.popen("nmcli dev wifi list | awk '/\*/{if (NR!=1) {print $10}}'").read()

while True:
	print("#" * int(wifimeter()))
	time.sleep(3)
