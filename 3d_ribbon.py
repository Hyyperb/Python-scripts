from math import *
import time

x = 0

def s(x,y,z):
    return int(sin(radians(x))*y)+z

while True:
    x += 1
    print(
        ("  "*s(x*4,10,20))+
        ("o"*s(x*4+20,2,4))+
        ("#"*s(x*4+20,3,6))+
        ("o"*s(x*4+20,10,20))+
        ("&"*s(x*4+40,3,6))
    )
    time.sleep(0.03)

