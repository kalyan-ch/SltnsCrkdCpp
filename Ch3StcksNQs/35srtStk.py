#implement a program to sort a stack such that smallest are on the top.
#O(N^2) time and O(N) extra Space

from Stack import Stack
from random import randint

def sort(stk):
	stk2 = Stack()
	while stk.getLen() !=0 :
		temp = stk.pop()
		while stk2.getLen() != 0 and stk2.peek() > temp:
			stk.push(stk2.pop())

		stk2.push(temp)

	return stk2


if __name__ == '__main__':	

	stk1 = Stack()


	for x in xrange(1,10):
		num = randint(1,100)
		stk1.push(num)

	stk1.printStack()

	#sorting begins
	stk2 = sort(stk1)

	stk2.printStack()



