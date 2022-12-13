import hashlib
import random
import time

def hash(key):
    return hashlib.md5("{}".format(key).encode()).hexdigest()

limit = 100000

answer = hash(input("enter a number within 100000: "))

if(answer == "random"):
    answer = hash(random.randint(1,limit))

print("The correct hash is: ",answer)
time.sleep(5)
print("\nrunning a stupid brute force attact")
time.sleep(2)

def checker(a,b):
    match = (a == b)
    if match:
        return "MATCHED"
    else:
        return "WRONG"

for x in range(limit):
    canswer = hash(x)
    print(x,": {} == {}    results:{}".format(canswer,answer,checker(answer,canswer)))
    if (answer == canswer):
        time.sleep(2)
        print("\nHECKED!!!1!")
        break
