def pow_ten(i):
	if i == 0:
		return 1

	return 10*pow_ten(i-1)


print pow_ten(5)