
def insertParens(stri,res):
	inds = [i for i, letter in enumerate(stri) if letter == "("]
	for x in inds:
		res.add(stri[0:x]+"()"+stri[x:])
		res.add(stri[0:x+1]+"()"+stri[x+1:])


def genParens(rem):
	res = set()

	if rem == 0:
		res.add("")
	else:	
		prev = genParens(rem-1)
		for x in prev:
			insertParens(x,res)
			res.add("()"+x)

	return res
	


if __name__ == '__main__':
	print genParens(4)
