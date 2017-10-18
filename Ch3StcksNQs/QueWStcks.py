from Stack import Stack

class NewQueue(object):
	
	def __init__(self):
		self.stkNew = Stack()
		self.stkOld = Stack()

	def push(self,data):
		self.stkNew.push(data)

	def shiftStks(self):
		if self.stkOld.getLen() == 0:
			while self.stkNew.getLen() != 0:
				self.stkOld.push(self.stkNew.pop())

	def pop(self):
		self.shiftStks()
		return self.stkOld.pop()


	def printQ(self):
		print "stack old"
		self.stkOld.printStack()
		print "stack new"
		self.stkNew.printStack()