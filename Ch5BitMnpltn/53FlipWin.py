import sys

def flipWin(num):
	
	if ~num == 0:
		return 8*(sys.getsizeof(0))

	maxLen = 1
	currLen = 0
	prevLen = 0
	while num != 0:
		if num&1 == 1:
			currLen += 1
		elif num&1 == 0:
			prevLen = currLen
			if num & 2 == 0:
				prevLen = 0
			currLen = 0

		print currLen , prevLen
		maxLen = max(currLen+prevLen+1, maxLen)
		num >>= 1

	return maxLen


if __name__ == '__main__':
	print flipWin(1775)
