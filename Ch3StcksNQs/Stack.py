class Stack(object):
	
	def __init__(self):
		self.dtList = []
		self.min = 1000000

	def push(self,data):
		if data < self.min:
			self.min = data
		self.dtList.append(data)

	def pop(self):
		temp = self.dtList[-1]
		del self.dtList[-1]
		return temp

	def getMin(self):
		return self.min

	def printStack(self):
		for x in self.dtList:
			print x,

		print ""

	def clearStk(self):
		self.dtList = []

	def getLen(self):
		return len(self.dtList)