nums={
	0:"zero",
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
}
tens={
	10:"ten",
	20:"twenty",
	30:"thirty",
	40:"fourty",
	50:"fifty",
	60:"sixty",
	70:"seventy",
	80:"eighty",
	90:"ninty"
}
teens={
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fifteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen"
}

def num_to_eng(n):
	
	if n<10:
		return nums[n]
		
	if 10<=n<100:
		if n%10==0:
			return tens[n]
		elif 10<n<20:
			return teens[n]
		else:
			return tens[n-n%10] + " " + nums[n%10]
			
	if n>=100:
		if n%100==0:
			return nums[(n-n%100)/100] + " hundred"
		elif n%10==0:
			return nums[(n-n%100)/100] + " hundred " + tens[int(str(n)[1])*10]
		elif n%100<10:
			return nums[(n-n%100)/100] + " hundred " + nums[int(str(n)[2])]
		elif 10<int(str(n)[1:])<20:
			return nums[(n-n%100)/100] + " hundred " + teens[int(str(n)[1:])]
		else:
			return nums[(n-n%100)/100] + " hundred " + tens[int(str(n)[1])*10] + " " + nums[int(str(n)[2])]
		
for i in range(1000):
	print(i,num_to_eng(i))