

def moveDisks(t1,t2,t3):
	n = len(t1)

	if n == 0:
		return

	moveDisks(t1[:-1],t2,t3)

	moveLast(t1,t3)

	moveDisks(t3,t2,t1)




if __name__ == '__main__':
	t1 = [x for x in range(1,3)[::-1]]
	t2 = []
	t3 = []

	moveDisks(t1,t2,t3)

	print t1,t2,t3
