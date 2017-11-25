#given a binary search tree. determine all possible orders they could have led to it

def getSeq(node):
	res = []
	prefix = [node.data]
	lefts = getSeq(node.left)
	rights = getSeq(node.right)

	for l in lefts:
		for r in rights:
			wv = []
			weaveLists(l,r,prefix,wv)
			res.append(wv)

	return res

def weaveLists(l,r,prefix,wv):
	if not l or not r:
		result = [x for x in prefix]
		result.extend(l)
		result.extend(r)
		wv.append(result)
		return

	hdl = l[0]
	del l[0]
	prefix.append(hdl)
	weaveLists(l,r,prefix,wv)
	del prefix[-1]
	l.insert(0,hdl)

	hdR = r[0]
	del r[0]
	prefix.append(hdR)
	weaveLists(l,r,prefix,wv)
	del prefix[-1]
	r.insert(0,hdR)

