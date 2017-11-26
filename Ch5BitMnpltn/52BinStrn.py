
def binRep(num):
	finStr = "."
	while num > 0:
		r = 2*num

		if r >= 1:
			finStr += "1"
			num = r - 1
		else:
			finStr += "0"
			num = r


	print finStr

