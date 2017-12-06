

def paintFill(screen,r,c,pxlClr,filClr):
	
	#dfs
	if screen[r][c] == pxlClr:
		screen[r][c] = filClr
		paintFill(screen,r-1,c,pxlClr,filClr)
		paintFill(screen,r+1,c,pxlClr,filClr)
		paintFill(screen,r,c-1,pxlClr,filClr)
		paintFill(screen,r,c+1,pxlClr,filClr)



if __name__ == '__main__':
	screen = [[0 for x in range(5)] for x in range(5)]
	for i in range(5):
		screen[1][i] = 1
		
		if i != 0:
			screen[i][4] = 1
			screen[i][0] = 1
		
		screen[4][i] = 1

	for x in screen:
		for y in x:
			print y,
		print 

	print ""
	paintFill(screen,2,2,0,2)

	for x in screen:
		for y in x:
			print y,
		print 

