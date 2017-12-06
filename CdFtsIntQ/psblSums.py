import copy

def getPerms(cnt_dic,prfx,rem,rs):
	for x in cnt_dic:
		cnt = cnt_dic[x]
		if cnt > 0:
			cnt_dic[x] = cnt-1
			l = list(prfx)
			l.append(x)
			nxt = tuple(l)
			rs.add(nxt)
			getPerms(cnt_dic,nxt,rem-1, rs)
			cnt_dic[x] = cnt



def possibleSums(coins,quantity):
	#freq dist
	cnt_dic = {}
	n = len(coins)

	for i in range(n):
		cnt_dic[coins[i]] = quantity[i]

	rs = set()
	prefix = ()
	getPerms(cnt_dic,prefix,n,rs)

	print rs
	return len(rs)

	

if __name__ == '__main__':
	print possibleSums([2,1,3],[1,1,1])