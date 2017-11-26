def updateBits(n,m,i,j):

	for x in range(i,j+1):
		mask = ~(1 << x)
		n &= mask


	n = n ^ (m << i)
	print n