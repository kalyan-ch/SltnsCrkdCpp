
#check if a binary tree is a binary search tree

def checkIfBST(root):
	
	return checkBST(root,None, None)

def checkBST(node, minn, maxx):
	if not node:
		return True

	#check if condition node.left.value <= node.value and node.value < node.right.value holds
	if ( minn != None and node.value <= minn ) or (maxx != None and node.value > maxx):
		return False

	#check the above condition recursively for left and right subtrees
	if (not checkBST(node.left, minn, node.value)) or (not checkBST(node.right, node.value, maxx)):
		return False

	return True