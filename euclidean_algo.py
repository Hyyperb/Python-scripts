import time

def gcd_log(x,y):
    while(y):
        print(f"{x},{y} = {y}, {x}%{y} ie {x%y}")
        x,y=y,x%y
        time.sleep(0.1)
    return x
    
def gcd_log2(x,y):
    while(y):
        print(f"{x}/{y} = {x-x%y}+{x%y}")
        x,y=y,x%y
        time.sleep(0.1)

if __name__=="__main__":
    gcd_log(128,116)
    print("-------")
    gcd_log2(128,116)