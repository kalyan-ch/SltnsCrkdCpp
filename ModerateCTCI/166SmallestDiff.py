# get smallest difference of a pair of values from two arrays

def getSmallDif(arr1,arr2):
	list.sort(arr1)
	list.sort(arr2)
	i,j = 0,0
	diff = abs(arr1[0]-arr2[0])
	
	while i < len(arr1) and j < len(arr2):
		if abs(arr1[i] - arr2[j]) < diff:
			diff = abs(arr1[i]-arr2[j])

		if arr1[i] < arr2[j]:
			i += 1
		else:
			j += 1


	return diff


if __name__ == '__main__':
	arr1 = [10,4,3,2,11,5]
	arr2 = [12,2,13,5,3,1,15]
	print getSmallDif(arr1,arr2)

