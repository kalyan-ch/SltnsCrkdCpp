class Stack(object):
	
	def __init__(self):
		self.dtList = []

	def push(self,data):
		self.dtList.append(data)

	def pop(self):
		if self.getLen() == 0:
			return None

		temp = self.dtList[-1]
		del self.dtList[-1]
		return temp

	def peek(self):
		if self.getLen() == 0:
			return None

		return self.dtList[-1]

	def getLen(self):
		return len(self.dtList)

	def printStack(self):
		for x in self.dtList[::-1]:
			print x,

		print ""

	def clearStk(self):
		self.dtList = []

	def getLen(self):
		return len(self.dtList)