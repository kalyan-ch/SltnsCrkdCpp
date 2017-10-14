from Stack import Stack

class NewQueue(object):
	
	def __init__(self):
		self.stk1 = Stack()
		self.stk2 = Stack()

	def push(self,data):
		self.stk1.push(data)

	def pop(self):
		self.stk2.clearStk()
		for x in range(self.stk1.getLen()-1,-1,-1):
			self.stk2.push(self.stk1.dtList[x])

		del self.stk1.dtList[0]
		return self.stk2.pop()


	def printQ(self):
		self.stk1.printStack()