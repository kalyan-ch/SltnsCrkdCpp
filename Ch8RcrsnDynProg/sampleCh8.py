

def fib(n):
	a = 0
	b = 1
	for i in range(2,n):
		c = a + b
		a = b
		b = c

	return a+b


if __name__ == '__main__':
	n = int(raw_input('Enter a number: '))
	
	print "Dynamic", fib(n)
	

