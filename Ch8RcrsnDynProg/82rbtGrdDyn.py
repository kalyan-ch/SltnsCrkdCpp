from random import randint

def moveRobot(maze):
	path = []
	cache = {}
	
	getPath(maze,len(maze)-1,len(maze[0])-1,path,cache)
	
	return path

def getPath(maze,row,col,path,cache):
	if row < 0 or col < 0 or maze[row][col] == "X":
		return False

	status = False
	if cache.get((row,col),"") != "":
		return cache[(row,col)]

	isAtOr = False
	if row == 0 and col == 0:
		isAtOr = True

	if (isAtOr or getPath(maze,row,col-1,path,cache) or getPath(maze,row-1,col,path,cache)):
		path.append((row,col))
		status = True

	cache[(row,col)] = status

	return status


if __name__ == '__main__':
	maze = [[0 for x in range(50)] for x in range(50)]
	
	for x in range(500):
		x = randint(0,49)
		y = randint(0,49)
		if not ((x == 49 and y == 49) or (x == 0 and y ==0)):
			maze[x][y] = "X"

	print 
	path = moveRobot(maze)

	for r,c in path:
		maze[r][c] = 1

	for x in maze:
		for y in x:
			print y,
		print


