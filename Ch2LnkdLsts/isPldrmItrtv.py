from LinkedList import LinkedList
import random


ll = LinkedList()
stack = []

def pop_stack():
	temp = stack[-1]
	del stack[-1]
	return temp

def isPalindrome():
	
	fast = ll.head
	slow = ll.head
	flag = True
	while (fast and fast.next):
		stack.append(slow.data)
		slow = slow.next
		fast = fast.next.next

	if fast:
		slow = slow.next

	while slow:
		if pop_stack() != slow.data:
			flag = False
			break
		slow = slow.next


	return flag

if __name__ == '__main__':
	
	ll.addNode(7)
	ll.addNode(2)
	ll.addNode(3)
	ll.addNode(2)
	ll.addNode(7)

	#for x in range(15):
	#	ll.addNode(random.randint(1,100))
	
	ll.printList()

	print "is the list a palindrome?",isPalindrome()

