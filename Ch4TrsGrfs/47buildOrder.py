graph = {}
visited = []
order = []
vertices = []
def addToOrder():
	for v in vertices:
		arr = graph.get(v,[])
		if not arr:
			if v not in order:
				order.append(v)

def getBuildOrder():
	
	addToOrder()
	ind = 0
	while ind < len(order):
		v = order[ind]
		for v1 in vertices:
			if v1 not in order:
				arr = graph.get(v1,[])
				if v in arr:
					del arr[arr.index(v)]
				graph[v1] = arr

		addToOrder()

		ind += 1


if __name__ == '__main__':
	vertices = ["a","b","c","d","e","f"]
	edges = [("d","a"),("b","f"),("d","b"),("a","f"),("c","d"),]

	#build graph
	for x,y in edges:
		arr = graph.get(x,[])
		arr.append(y)
		graph[x] = arr

	print graph
	getBuildOrder()
	print order



