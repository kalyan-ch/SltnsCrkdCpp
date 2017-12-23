#get max of two numbers
#don't use if else 
def flip(a):
	return 1^a

def sign(a):
	return flip(a>>31 & 0x1)

def getMax(a,b):
	k = sign(a-b)
	q = flip(k)
	return a * k + b * q


if __name__ == '__main__':
	print getMax(12426561,21542645)


