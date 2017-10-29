
def treeDiameter(n, tree):
    pathMax = 0
    #convert into dict
    dct_grp = {}
    for arr in tree:
        arr1 = dct_grp.get(arr[0],[])
        arr1.append(arr[1])
        dct_grp[arr[0]] = arr1

    this_level = tree[0]

    while this_level:
        next_level = []

        for x in this_level:
            print x,
            arr = dct_grp.get(x,[])
            if arr:
                for y in arr:
                    next_level.append(y)

        this_level = next_level
        

    return pathMax



if __name__ == '__main__':
    tr = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], [7, 6], [6, 3], [3, 8], [8, 4]]
    treeDiameter(10,tr)

