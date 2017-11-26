
def getHeavyBottle(arr,pillWt,exWt):
	weight = 0
	n = len(arr)
	for i in range(n):
		print arr[i][:i+1]
		weight += sum(arr[i][:i+1])

	expWt = (n*(n+1))/2
	expWt *= pillWt
	print expWt,weight,exWt
	return (weight - expWt) / exWt


if __name__ == '__main__':
	print getHeavyBottle([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2.2,2.2,2.2,2.2,2.2]],2,2.2)