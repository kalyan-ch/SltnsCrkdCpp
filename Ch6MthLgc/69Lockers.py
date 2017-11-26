def lockerToggle(i,arr):
	for x in range(len(arr)):
		if (x+1) % i == 0:
			if arr[x] == 0:
				arr[x] = 1
			else:
				arr[x] = 0


def numOfOpen(arr):
	for i in range(2,100+1):
		lockerToggle(i,arr)

	count = 0
	for i in range(len(arr)):
		if arr[i] == 1:
			count += 1 
			print i+1
	return count

if __name__ == '__main__':
	arr = [1 for x in range(100)]
	print numOfOpen(arr)