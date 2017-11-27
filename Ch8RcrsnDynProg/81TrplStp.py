
def numWays(n, memo):
	a = 0
	b = 1
	c = 1

	for x in range(2,n):
		d = a + b + c
		a = b
		b = c
		c = d

	return a + b + c

if __name__ == '__main__':
	n = int(raw_input('Enter number of steps: '))
	memo = [-1 for x in range(n+1)]
	print numWays(n,memo)