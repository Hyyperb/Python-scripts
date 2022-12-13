import time
from math import *

x = 0
ml = "||"

def sine(d,c,w):
	return int(sin(radians(d))*c)+w

while True:
	time.sleep(0.05)
	x+=1
	if x % 5 == 0:
		ml = "--"
	else:
		ml = "11"
	print(" "*sine(x*2,50,50),"   ##-------{}-------##".format(ml))
