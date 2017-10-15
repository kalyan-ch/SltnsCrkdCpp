
#check rows, columns and 3x3 grids

def checkDupsRow(arr):
    arr1 = [0 for x in range(9)]
    for num in arr:
        try:
            num1 = int(num)
            arr1[num1-1] += 1
        except Exception as e:
            pass

    for y in arr1:
        if y > 1:
            return False

    return True


def checkCol(grid,col):
    n = len(grid)
    arr1 = [0 for x in range(9)]
    
    for x in range(n):
        try:
            num1 = int(grid[x][col])
            arr1[num1] +=1
        except Exception as e:
            pass

    for y in arr1:
        if y > 1:
            return False

    return True

def checkGrid(grid, x, y):
    indx = x*3
    indy = y*3

    arr1 = [ 0 for x in range(9)]

    for i in range(indx,indx+3):
        for j in range(indy,indy+3):
            try:
                num1 = int(grid[i][j])
                arr1[num1] +=1
            except Exception as e:
                pass


    for x in arr1:
        if x > 1:
            return False

    return True


def checkGrids(grid):
    for i in range(3):
        if not checkGrid(grid,0,i):
            return False
        if not checkGrid(grid,1,i):
            return False
        if not checkGrid(grid,2,i):
            return False

    return True

        


def sudoku2(grid):
    n = len(grid)

    for i in range(n):
        if not checkDupsRow(grid[i]):
            return False

        if not checkCol(grid,i):
            return False

    if not checkGrids(grid):
        return False

    return True




