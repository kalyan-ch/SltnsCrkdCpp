sumList = []

def getPathSum(node, res):
    res += node.value
    if (not node.left) and (not node.right):
        sumList.append(res)
    
    else:
        if node.left:
            getPathSum(node.left,0)
        if node.right:
            getPathSum(node.right,0)




def hasPathWithGivenSum(t, s):
    getPathSum(t,0)
    print sumList

