



def isRoute(adjList, node1, node2):
	if not adjList:
		return False
	if node1 == node2:
		if node1 in adjList[node1]:
			return True

	visited = []

	this_level = [node1]

	while this_level:
		next_level = []

		for x in this_level:
			for y in adjList[x]:
				if y not in visited:
					if y == node2:
						return True
					else:
						visited.append(y)
						next_level.append(y)

		this_level = next_level


	return False

if __name__ == '__main__':
	adjList = {}
	adjList[0] = [1]
	adjList[1] = [5,2]
	adjList[2] = [3]
	adjList[3] = [2,4]
	adjList[4] = [6]
	adjList[5] = [4]
	
	
	node1 = 0
	node2 = 5
	
	print isRoute(adjList, node1, node2)
