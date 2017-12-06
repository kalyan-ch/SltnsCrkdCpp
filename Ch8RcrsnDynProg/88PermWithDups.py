def buildPerms(cnt_dic, prfx,rem,res):
	print prfx,rem
	if rem == 0:
		res.append(prfx)
		return

	for x in cnt_dic:
		cnt = cnt_dic[x]
		if cnt > 0:
			cnt_dic[x] = cnt-1
			buildPerms(cnt_dic,prfx+x,rem-1, res)
			cnt_dic[x] = cnt



def getFreq(s):
	cnt_dic = {}
	for x in s:
		num = cnt_dic.get(x,0)
		num += 1
		cnt_dic[x] = num

	return cnt_dic

def getPerms(s):
	cnt_dic = getFreq(s)
	res = []
	buildPerms(cnt_dic,"",len(s),res)
	return res

if __name__ == '__main__':
	print getPerms("aab")