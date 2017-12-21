#get number of zeros in a factorial of a number

def getFactZeros(n):
	fives = 0
	twos = 0

	for i in range(1,n+1):
		x = i
		while x%5 == 0:
			fives += 1
			x = x/5

		y = i
		while y%2 == 0:
			twos += 1
			y = y/2

	return min(fives,twos)


if __name__ == '__main__':
	print getFactZeros(1000)