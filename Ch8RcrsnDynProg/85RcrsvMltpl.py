def multiply(a,b):
	res = 0

	if a < b:
		for x in range(b):
			res += a
	else:
		for x in range(a):
			res += b

	return res


if __name__ == '__main__':
	print multiply(1,5789)