from BT import BTNode

#check if a binary tree is balanced
#balanced = right and left subtrees should only differ 1 in their heights

def gtHeight(node):
	if not node:
		return -1
	return max([gtHeight(node.left),gtHeight(node.right)])+1

def checkBalanced(root):
	if not root:
		return True

	return gtHeight(root) != -1


def createBST(arr,start,end):
	
	if end < start:
		return None

	mid = (start+end)/2
	n = BTNode(arr[mid])

	n.left = createBST(arr,start,mid-1)
	n.right = createBST(arr,mid+1,end)

	return n


if __name__ == '__main__':
	arr =  [x for x in range(10)]
	print arr
	root = createBST(arr,0,len(arr)-1)
	print root.left, root.right

	print gtHeight(root)
	


