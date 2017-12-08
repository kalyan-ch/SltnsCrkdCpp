dens = [25,10,5,1]

def makeCh(n,hmap,ind):
	if hmap.get((n,ind),0) > 0:
		return hmap[(n,ind)]

	if ind >= len(dens):
		return 1
	
	d = dens[ind]
	
	i = 0
	ways = 0
	while i*d <= n:
		an = n - i*d
		ways += makeCh(an,hmap,ind+1)
		i += 1

	hmap[(n,ind)] = ways
	print hmap
	return ways



def makeChange(n):
	hmap = {}	
	return makeCh(n,hmap,0)



if __name__ == '__main__':
	print makeChange(10)
