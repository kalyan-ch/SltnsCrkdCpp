#get fisrt common ancestor of two nodes in binary tree
#solution with links to parents

def checkQ(node,q):
	if not node:
		return null
	if node == q:
		return True

	return checkQ(node.left,q) || checkQ(node.right,q)

def getSibling(node):
	if (not node) or (not node.parent):
		return null
	parent = node.parent
	if parent.left == node:
		return parent.right
	else:
		return parent.left

def getAncestor(node1,node2):
	p = node1
	q = node2

	node = p.parent
	sib = getSibling(p)
	while !checkQ(sib,q):
		p = p.parent

	return node
