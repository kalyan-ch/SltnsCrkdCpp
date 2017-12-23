# given k plans and two types of planks shrt and lng. 
# figure out number of ways they can be added and get all lengths of those ways

def diveBoards(k,shrt,lng):
	res = set()
	for x in range(0,k+1):
		y = k - x
		l = x*shrt + y*lng
		res.add(l)
	return res


if __name__ == '__main__':
	print list(diveBoards(20,2,5))


