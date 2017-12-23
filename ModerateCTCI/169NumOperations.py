# perform subtraction, multiplication and division operations on numbers without using the obvious operators.
# addition is allowed

def negate(a):
	neg = 0

	sign = -1
	if a < 0:
		sign = 1
	
	while abs(neg) < abs(a):
		neg += sign
	
	return neg

# idea: a + -1*b
def substract(a,b):
	return a + negate(b)

def multiply(a,b):
	res = 0
	
	for x in range(abs(b)):
		res += abs(a)

	if (a < 0) ^ (b < 0):
		res = negate(res)

	return res

def divide(a,b):
	if b == 0:
		return None

	prod = 0
	i = 0
	while prod + abs(b) <= abs(a):
		prod += abs(b)
		i += 1

	if (a < 0) ^ (b < 0):
		i = negate(i)
	return i


if __name__ == '__main__':
	a = 10
	b = -5
	print substract(a,b)
	print multiply(a,b)
	print divide(a,b)
