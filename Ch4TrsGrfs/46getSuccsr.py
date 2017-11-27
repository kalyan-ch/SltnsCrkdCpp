# write an algorithm that gets the next node (in order successor) of a node in binary search tree. Nodes have links to parents
# successor of a mid-level node is the left-most node of right subtree.

def getLeftMostNode(n):
	while n.left:
		n = n.left

	return n

def getSuccessor(node):

	#right node exists
	if node.right:
		n_left = getLeftMostNode(node.right)
		return n_left

	#doesn't exist
	else:
		q = node
		x = q.parent
		
		#get the parent that is not fully traversed of node that is fully traversed
		while x and x.left != q:
			q = x
			x = q.parent
		return x


