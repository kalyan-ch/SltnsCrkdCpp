from BT import BTNode
from QueCh4 import Queue
from random import randint


def BFS(root):
	result = []
	this_level = [root]

	while this_level:
		result.append(this_level)
		
		next_level = []

		for node in this_level:
			
			if node.left:
				next_level.append(node.left)
			if node.right:
				next_level.append(node.right)

		this_level = next_level
	
	return result


def DFS(node):
	if not node:
		return None

	print node.value

	if node.left:
		DFS(node.left)
	if node.right:
		DFS(node.right)




def createBST(arr,start,end):
	
	if end < start:
		return None

	mid = (start+end)/2
	n = BTNode(arr[mid])

	n.left = createBST(arr,start,mid-1)
	n.right = createBST(arr,mid+1,end)

	return n

def inorder(node):
	if node:
		inorder(node.left)
		print node.value,
		inorder(node.right)


if __name__ == '__main__':
	arr = []

	for x in range(20):
		arr.append(randint(1,1000))

	arr.sort()
	
	print arr

	root = createBST(arr,0,len(arr)-1)
	
	
	print
	print "Tree"
	for x in BFS(root):
		for y in x:
			print y,
		print
	print
	


	DFS(root)

	