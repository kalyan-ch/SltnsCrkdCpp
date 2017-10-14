from Stack import Stack
from Queue import Queue
import random

stack = Stack()
que = Queue()

for x in range(10):
	num = random.randint(-10,10)
	stack.push(num)
	print num,
	print "Min element in stack = ",stack.getMin()
	que.push(num)

print "Push Order"

stack.printStack()
que.printQ()



