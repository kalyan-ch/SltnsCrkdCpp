from BT import BTNode

def inorder(node):
	if node:
		inorder(node.left)
		print node.value,
		inorder(node.right)

def preorder(node):
	if node:
		print node.value,
		preorder(node.left)		
		preorder(node.right)

def createBST(arr,start,end):
	
	if end < start:
		return None

	mid = (start+end)/2
	n = BTNode(arr[mid])

	n.left = createBST(arr,start,mid-1)
	n.right = createBST(arr,mid+1,end)

	return n




arr =  [x for x in range(10)]
print arr

root = createBST(arr,0,len(arr)-1)

inorder(root)
print ""
preorder(root)
print ""

