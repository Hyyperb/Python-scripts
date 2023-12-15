import pandas as pd
import matplotlib.pyplot as plt

arr = []
data = {}
for y in range(7):
    y+=1
    for x in range(100):
        if y == 1:
            break
        if y%2==0:
            y /= 2        
        else:
            y = y*3+1
        arr.append(y)
    data[y] = arr

df = pd.DataFrame(data)
df.plot()

plt.show()
