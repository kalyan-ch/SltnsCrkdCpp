from Stack import Stack

class SetOfStacks(object):
	
	def __init__(self):
		self.stackSet = []
		self.thres = 10

	def pushStack(self):
		stk = Stack()
		self.stackSet.append(stk)

	def push(self,data):
		if len(self.stackSet) == 0:
			self.pushStack()

		stk = self.stackSet[-1]
		if stk.getLen() <10:
			stk.push(data)
		else:
			self.pushStack()
			self.stackSet[-1].push(data)

	def pop(self):
		stk = self.stackSet[-1]
		if stk.getLen() > 0:
			return stk.pop()
		else:
			del self.stackSet[-1]
			return self.stackSet[-1].pop()


	def printSet(self):
		for stk in self.stackSet:
			stk.printStack()

		