from Node import Node
class LinkedList(object):
	
	def __init__(self):
		self.head = None


	def addNode(self,data):
		n = Node(data)
		hd = self.head
		if hd:
			a = hd
			
			while True:
				if a.next == None:
					break
				a = a.next

			a.next = n
		else:
			self.head = n

	def printList(self):
		hd = self.head
		while hd:
			
			if hd.next:
				print str(hd.data)+"->",
			else:
				print hd.data
			
			hd = hd.next
		