#return a random node from the tree
# every node should be returned with a probability of 1/n - n = number of nodes in the tree
from random import randint

class Tree(object):
	def __init__(self):
		self.root = None

	def getRandomNode(self):
		if not self.root:
			return None
		ind = randint(0,self.root.size)
		return self.root.getIthNode(ind)

	def insertNode(self,data):
		if not self.root:
			self.root = TreeNode(data)
		else:
			self.root.insertNode(data)

	def inorder(self,node):
		if node:
			self.inorder(node.left)
			print node.value,
			self.inorder(node.right)


class TreeNode(object):
	
	def __init__(self, data):
		self.value = data
		self.left = None
		self.right = None
		self.size = 1

	def getIthNode(self,i):
		leftSize = 0
		if self.left:
			leftSize = self.left.size

		if i < leftSize:
			return self.left.getIthNode(i)
		elif(i == leftSize):
			return self
		else:
			return self.right.getIthNode(i - (leftSize+1))

	def insertNode(self,data):
		if data <= self.value:
			if self.left:
				self.left.insertNode(data)
			else:
				self.left = TreeNode(data)
		else:
			if self.right:
				self.right.insertNode(data)
			else:
				self.right = TreeNode(data)

		self.size += 1

	
if __name__ == '__main__':
	t = Tree()
	t.insertNode(20)
	t.insertNode(40)
	t.insertNode(10)
	t.insertNode(5)
	t.insertNode(25)
	t.insertNode(15)
	t.inorder(t.root)
	print 

	print t.getRandomNode()
