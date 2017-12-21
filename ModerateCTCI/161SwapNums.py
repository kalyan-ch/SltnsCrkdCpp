
def swap(a,b):
	a = a ^ b
	b = b ^ a
	a = a ^ b

	return a,b



if __name__ == '__main__':
	a = 5
	b = 10
	a,b = swap(a,b)
	print a,b