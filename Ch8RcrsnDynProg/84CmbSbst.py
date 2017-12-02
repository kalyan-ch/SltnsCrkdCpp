

def comb(i,a):
	res = []
	for x in a:
		arr = [x]
		
	return res


def getSubsets(a):
	res = []
	for i in range(len(a)):
		res.extend(comb(i,a))

	return res


if __name__ == '__main__':
	print getSubsets([1,2])

