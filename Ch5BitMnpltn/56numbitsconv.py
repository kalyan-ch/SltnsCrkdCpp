
def numBits(a,b):
	c = a^b
	cnt = 0
	while c != 0:
		if c & 1 != 0:
			cnt += 1
		c >>= 1

	return cnt

if __name__ == '__main__':
	print numBits(13948,1024)