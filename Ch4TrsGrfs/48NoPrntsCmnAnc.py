#get fisrt common ancestor of two nodes in binary tree
#solution without links to parents

def checkQ(node,q):
	if not node:
		return null
	if node == q:
		return True

	return checkQ(node.left,q) || checkQ(node.right,q)

def getAncestor(root, p,q):
	if not root or root == p or root == q:
		return root

	pleft = checkQ(root.left,p)
	qleft = checkQ(root.left,q)

	if pleft != qleft:
		return root

	child = None
	if pleft:
		child = root.left
	else:
		child = root.right

	return getAncestor(child,p,q)


