import copy
def addChar(lst,c):

	rs = []
	for s in lst:
		for i in range(len(s)+1):
			rs.append(s[:i]+c+s[i:])

	return rs

def getAllPerms(s):
	if not s:
		return None

	if len(s) == 1:
		return [s[0]]

	res = getAllPerms(s[:-1])
	rst = copy.deepcopy(res)
	rs = addChar(rst,s[-1])

	return rs

if __name__ == '__main__':
	stri = ""
	for x in (getAllPerms("wolfblade")):
		stri += x+" ,"

	with open("res.txt","w") as f:
		f.write(stri)

