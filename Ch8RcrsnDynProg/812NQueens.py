import copy

grid_size = 4

#grid is represented by a single array cols with numbers indicating on which row the queen is placed

#checks each row and column and checks if conflicts exist.
def placeQueens(row,cols,res):
	if row == grid_size:
		cls = copy.deepcopy(cols)
		res.append(cls)
	else:
		for c in range(grid_size):
			if checkValid(cols,row,c):
				cols[row] = c
				placeQueens(row+1,cols,res)

#conflick checker - col and diagonal. row is already taken care of because calling this method once per row
def checkValid(cols,row,c):
	print row,c
	for r in range(row):
		if cols[r] == c:
			return False
		rd = row - r
		cd = abs(cols[r]-c)
		print r,c,rd,cd
		if rd-cd == 0:
			return False
	return True


if __name__ == '__main__':
	res = []
	cols = [0 for x in range(grid_size)]
	placeQueens(0,cols,res)
	print res


