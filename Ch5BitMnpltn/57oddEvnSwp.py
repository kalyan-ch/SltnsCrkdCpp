
def oddEvenSwap(num):
	return  ((num & 0xaaaaaa) >> 1) | ((num & 0x555555) << 1)

if __name__ == '__main__':
	print oddEvenSwap(658)