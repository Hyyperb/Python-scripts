import random

def test():
	deck = range(52)
	hand = []
	for i in range(9):
		hand.append(random.choice(deck))
	if 1 in hand and 2 in hand and 3 in hand:
		return 1
	return 0

tests = 50000
count = 0

for i in range(tests):
	if i % 1000 == 0:
		print(i)
	count += test()

print(count)
print(count/tests*100,"%")
