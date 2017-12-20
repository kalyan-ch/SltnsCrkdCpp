import copy

tree = {}

def treeDFS(node,paths,path):
    arr = tree.get(node,[])
    flag = True
    path.append(node)
    
    if not arr:
        pth = copy.deepcopy(path)
        paths.append(pth)
        path.pop()
        flag = False

    for x in arr:
        treeDFS(x,paths,path)

    if path and flag:
        path.pop()

    

def getLongPath(node):
    path = []
    paths = []
    treeDFS(node,paths,path)
    maxPth = []
    for x in paths:
        if len(x) > len(maxPth):
            maxPth = x

    return "/".join(maxPth)

def getParent(sArr,x):
    ind = sArr.index(x)
    tmp = sArr[ind-1]
    tcnt = tmp.count("\t")
    
    if abs(tcnt - x.count("\t")) == 1:
        return tmp
    else:
        return getParent(sArr,tmp)

def longestPath(s):
    sArr = s.split("\r")
    fr = sArr[0]
    tree[fr] = []

    for x in sArr:
        print x
    
    for x in sArr[1:]:
        if x.count("\t") == 1:
            tree[fr].append(x.strip())
        else:
            parent = getParent(sArr,x)
            parent = parent.strip()
            arr = tree.get(parent,[])
            arr.append(x.strip())
            tree[parent] = arr

    path = getLongPath(fr)
    return len(path)


if __name__ == '__main__':
    s = "dir\r\tfile.txt"
    print longestPath(s)