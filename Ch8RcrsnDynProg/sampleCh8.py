def fact(num):
	prod = 1
	for x in range(1,num+1):
		prod *= x
	return prod

if __name__ == '__main__':
	print fact(8)