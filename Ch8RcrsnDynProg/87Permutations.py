
#adds the character c to every position in each string of lst
def addChar(lst,c):

	rs = []
	for s in lst:
		for i in range(len(s)+1):
			rs.append(s[:i]+c+s[i:])

	return rs

#idea - get permutations of s[:-1] and add s[-1] to each permutation
def getAllPerms(s):
	if not s:
		return None

	if len(s) == 1:
		return [s[0]]
	rs = []
	res = getAllPerms(s[:-1])
	rs.extend(addChar(res,s[-1]))

	return rs

#test
if __name__ == '__main__':
	stri = ""
	for x in (getAllPerms("wolf")):
		stri += x+" ,"

	with open("res.txt","w") as f:
		f.write(stri)

