class Queue(object):
	
	def __init__(self):
		self.dtList = []
	
	def push(self,data):
		self.dtList.append(data)

	def pop(self):
		temp = self.dtList[0]
		del self.dtList[0]
		return temp
	def printQ(self):
		for x in self.dtList:
			print x,

		print ""
