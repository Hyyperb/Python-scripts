
def factorial(n):
	if n>1:
		return n * factorial(n-1)
	else:
		return 1

inp = int(input("enter number: "))
print(factorial(inp))

