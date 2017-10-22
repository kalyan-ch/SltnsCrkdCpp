from minHeap import MinHeap
from random import randint
mh = MinHeap()
arr = []
for x in range(20):
	num = randint(1,100)
	mh.insert(num)
	arr.append(num)

mh.printHeap()
print mh.extract_min()
mh.printHeap()