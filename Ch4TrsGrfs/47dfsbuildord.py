vertices = []
graph = {}
visited = []
order = []

def dfs(node):
	if node not in visited:
		visited.append(node)
		arr = graph.get(node,[])
		for x in arr:
			dfs(x)
		order.append(node)


def getBuildOrder():
	for x in vertices:
		if x not in visited:
			dfs(x)



if __name__ == '__main__':
	vertices = ["a", "b", "c", "d", "e", "f", "g"]
	edges = [("b","c"),("a","e"),("d","g"),("f","c"),("b","d"),("a","c"),("g","a"),("e","b")]

	#build graph
	for x,y in edges:
		arr = graph.get(x,[])
		arr.append(y)
		graph[x] = arr

	getBuildOrder()
	print graph
	print order
