#implement 3 stacks in a single array

from StackArray import StacksArrayFixd

from random import randint

stkArr = StacksArrayFixd(6)

for i in range(18):
	inde = 0
	if i <6:
		inde = 1
	elif i < 12:
		inde = 2
	else:
		inde = 3	

	stkArr.push(inde,randint(1,100))


stkArr.printArr()


for i in range(6):
	print stkArr.pop(3)


stkArr.printArr()
