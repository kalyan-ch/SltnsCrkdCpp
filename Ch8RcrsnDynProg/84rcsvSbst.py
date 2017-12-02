import copy

def addEtoSet(rs, e):
	
	for x in rs:
		x.append(e)
	return rs
	

def getSubsets(or_set):
	n = len(or_set)
	if n == 0:
		return [[]]

	e = or_set.pop();
	res = getSubsets(or_set)
	rs = copy.deepcopy(res)
	addEtoSet(rs,e)

	res.extend(rs)

	return res


if __name__ == '__main__':
	print getSubsets([x for x in range(3)])


