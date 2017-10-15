#fixed size for each stack

#stack indexes
#stack 1 = 0,n/3-1
#stack 2 = n/3,2n/3-1
#stack 1 = n/3,n-1

class StacksArrayFixd(object):
	
	def __init__(self, size):		
		self.stkSize = size
		self.n = size*3
		self.arr = [0 for x in range(self.n)]
		self.stkInds = [0 for x in range(3)]


	def isFull(self,stkNum):
		if self.stkInds[stkNum-1] == self.stkSize:
			return True
		
		return False

	def insIndex(self,stkNum):
		ind = self.stkSize * (stkNum-1)
		index = ind+self.stkInds[stkNum-1]
		return index

	def popIndex(self,stkNum):
		ind = (self.stkInds[stkNum-1] - 1) + (self.stkSize * (stkNum-1))
		return ind

	def push(self,stkNum,data):
		if not self.isFull(stkNum):
			self.arr[self.insIndex(stkNum)] = data
			self.stkInds[stkNum-1]+=1
			return True
		else:
			return False


	def pop(self,stkNum):
		if self.stkInds[stkNum-1] == 0:
			return None

		ind = self.popIndex(stkNum)
		temp = self.arr[ind]
		self.arr[ind] = 0
		self.stkInds[stkNum-1] -= 1

		return temp


	def printArr(self):
		for x in self.arr:
			print x,

		print ""
		