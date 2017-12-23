def insertDic(year_dc,st):
	num = year_dc.get(st,0)
	num += 1
	year_dc[st] = num

def getLongestYear(data):
	year_dc = {}
	minY = 1900
	maxY = 2000
	for tup in data:
		pId,st,en = tup
		if (st >= 1900 and st <= 2000) and (en >= 1900 and en <=2000):
			insertDic(year_dc,st)
			insertDic(year_dc,en)

	maxNum = 0

	for x in year_dc:
		if year_dc[x] > maxNum:
			maxNum = year_dc[x]

	return maxNum


if __name__ == '__main__':
	data = []
	getLongestYear(data)