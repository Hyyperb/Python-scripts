import os
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np
import random
import time

def exam():
	pad = 15 #not in use rn
	marks = 0

	for question in range(65):
		if not random.randint(0,2):
			print(f" = {marks} + 4")
			marks+=4
		else:
			print(f" = {marks}  - 1")
			marks-=1

		""" 
		if marks>0:
			print(" "*pad+"|"+"#"*marks)
		else:
			print(" "*(pad+marks)+"#"*marks+"|")
		"""
		
			
	print(f"= {marks}")
	return marks

nexams = 10000

exams = np.empty(nexams)

for i in range(nexams):
	e = exam()
	exams[i] = e

max = exams.max()
min = exams.min()
mean = exams.mean()
stddev = exams.std()

# plt.plot(exams)

print(mean)
print(max)
print(min)
print(stddev)

x_axis = np.arange(mean-3.5*stddev,mean+3.5*stddev, 0.01)

plt.plot(x_axis, norm.pdf(x_axis, mean, stddev))
plt.show()

# 40k test result:
# mean: 12.588125
# max: 85.0
# min: -45.0
