#implement a queue with two stacks

from QueWStcks import NewQueue
from random import randint


qu = NewQueue()


qu.push(randint(1,100))
qu.push(randint(1,100))
qu.push(randint(1,100))
qu.push(randint(1,100))
print "before"
qu.printQ()
print qu.pop()
print qu.pop()

qu.push(randint(1,100))
print "after"

qu.printQ()

