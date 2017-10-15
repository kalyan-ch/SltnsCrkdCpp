#implement a set of stacks like real world piles of plates

from SetOfStacks import SetOfStacks
from random import randint
stkSt = SetOfStacks()

for x in range(34):
	stkSt.push(randint(1,100))

stkSt.printSet()

for x in range(34):
	print stkSt.pop(),