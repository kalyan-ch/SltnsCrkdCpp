# check if one tree is a subtree of the other bigger tree
#t1- bigger and t2- smaller, check if t2 is bigger than t1
#alternative solution
#Search bigger tree for root of smaller one. Recursively check if tree is subtree by comparing all nodes

def matchtree(node1,node2):
	if node1 and node2:
		if (node1.value == node2.value) and matchtree(node1.left, node2.left) and matchtree(node1.right, node2.right):
			return True
		else:
			return False
	else if (not node1) and (not node2):
		return True
	else:
		return False



def chkSubTree(t1,t2):
	this_level = [t1]

	while this_level:
		for node in this_level:
			next_level = []
			if node.value == t2.value:
				if matchtree(node,t2):
					return True
			if node.left:
				next_level.append(node.left)
			if node.right:
				next_level.append(node.right)

		this_level = next_level
