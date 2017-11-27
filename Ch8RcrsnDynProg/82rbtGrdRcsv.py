from random import randint

def moveRobot(maze):
	h = len(maze)
	w = len(maze[0])
	r,c = h-1,w-1
	path = []
	if(getPath(maze,r,c,path)):
		return path
	return None

def getPath(maze,row,col,path):
	if row < 0 or col < 0 or maze[row][col] == 2:
		return False

	isAtOr = False
	
	if row == 0 and col == 0:
		isAtOr = True

	if (isAtOr or getPath(maze,row,col-1,path) or getPath(maze,row-1,col,path)):
		path.append((row,col))
		return True

	return False

if __name__ == '__main__':
	maze = [[0 for x in range(50)] for x in range(50)]
	
	for x in range(500):
		x = randint(0,49)
		y = randint(0,49)
		if not ((x == 49 and y == 49) or (x == 0 and y ==0)):
			maze[x][y] = 2

	for x in maze:
		for y in x:
			print y,
		print

	print 
	path = moveRobot(maze)
	if path:
		for r,c in path:
			maze[r][c] = 1

		for x in maze:
			for y in x:
				print y,
			print




