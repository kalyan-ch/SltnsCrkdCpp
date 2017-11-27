
def swapNumbers(x,y):
	print x,y
	x = x ^ y
	y = y ^ x
	x = y ^ x
	print x,y

if __name__ == '__main__':
	swapNumbers(20,25)