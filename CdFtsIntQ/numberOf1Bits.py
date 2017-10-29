def numberOf1Bits(n):
    res = 0
    count = 0
    while n != 0:
    	mask = 1 << count
    	
    	num = n & mask
    	n = n ^ num
    	
    	if num != 0:
    		res += 1

    	count += 1

    return res


if __name__ == '__main__':
	print numberOf1Bits(51)