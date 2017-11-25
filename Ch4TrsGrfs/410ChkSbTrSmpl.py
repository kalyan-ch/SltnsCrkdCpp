# check if one tree is a subtree of the other bigger tree
#t1- bigger and t2- smaller, check if t2 is bigger than t1
#simple solution
#take pre-order traversals of both trees and see if one is substring of another


def preOrder(node,arr):
	if node:
		arr.append(node)
		preOrder(node.left,arr)
		preOrder(node.right,arr)
	else:
		arr.append("X")

def checkSubTree(t1,t2):
	arr = []
	preOrder(t1.root,arr)
	arr2 = []
	preOrder(t2.root,arr2)

	for x in arr2:
		if x not in arr:
			return False

	return True

