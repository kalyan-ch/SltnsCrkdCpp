# check if a player has won the game of tic tac toe
def hasCol(grid,col):

	for x in range(len(grid)):
		if grid[x][col] != "O":
			return False

	return True

def hasRow(grid,row):

	for x in range(len(grid)):
		if grid[row][x] != "O":
			return False

	return True

def hasDia(grid):
	dia1 = True
	n = len(grid)
	for x in range(n):
		if grid[x][x] != "O":
			dia1 = False

	y = len(grid)-1
	dia2 = True
	for x in range(n):
		print x,y
		if grid[x][y] != "O":
			dia2 = False
		y -= 1

	if dia1 or dia2:
		return True

	return False

def ticTacWin(grid):
	n = len(grid)
	
	hsCl = False
	for col in range(n):
		if hasCol(grid,col):
			hsCl = True

	hsRw = False
	for row in range(n):
		if hasRow(grid,row):
			hsRw = True
	
	if hasDia(grid) or hsRw or hsCl:
		return True

	return False

if __name__ == '__main__':
	grid = [["O","X","-"],["X","O","X"],["X","X","O"]]
	print ticTacWin(grid)