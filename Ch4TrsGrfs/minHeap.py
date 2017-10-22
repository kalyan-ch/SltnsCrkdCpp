
class MinHeap(object):
	def __init__(self):
		self.heap = []

	#indexes
	def getprntInd(self,ind):
		return (ind-1)/2

	def getLeftInd(self,ind):
		return (ind*2 + 1)

	def getRightInd(self,ind):
		return (ind*2 + 2)
	
	#swap
	def swap(self, ind1, ind2):
		temp = self.heap[ind1]
		self.heap[ind1] = self.heap[ind2]
		self.heap[ind2] = temp

	#insert
	def insert(self,value):
		self.heap.append(value)
		self.heapifyUp()

	#extract min
	def extract_min(self):
		lastind = len(self.heap)
		if lastind != 0:
			temp = self.heap[0]
			self.heap[0] = self.heap[lastind-1]
			del self.heap[lastind-1]
			lastind-=1
			self.heapifyDown();

			return temp


	#actual fun
	def heapifyUp(self):

		ind = len(self.heap)-1
		parent = self.getprntInd(ind)
		par_ele = self.heap[parent]
		curr_ele = self.heap[ind]
		
		while (parent >=0) and ( par_ele > curr_ele ) :
			self.swap(parent,ind)
			ind = parent
			parent = self.getprntInd(ind)
			par_ele = self.heap[parent]
			curr_ele = self.heap[ind]

	def heapifyDown(self):
		ind = 0
		left = self.getLeftInd(ind)

		size = len(self.heap)

		while left < size:
			smlInd = left
			right = self.getRightInd(ind)
			if right < size and self.heap[right] < self.heap[left]:
				smlInd = right

			if self.heap[ind] < self.heap[smlInd]:
				break
			else:
				self.swap(ind,smlInd)

			ind = smlInd
			left = self.getLeftInd(ind)

	def printHeap(self):
		print self.heap