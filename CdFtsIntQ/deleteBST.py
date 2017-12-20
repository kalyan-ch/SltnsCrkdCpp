#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def dfsGetNode(node,x):
    if node:
        if node.left.value == x or node.right.value == x:
            return node
        dfsGetNode(node.left,x)
        dfsGetNode(node.right,x)

def deleteNode(node,x):
    pass

def deleteFromBST(t, queries):

    for x in queries:
        if x == t.value:
            pass
        else:
            node = dfsGetNode(t,x)
            if node:
                x = deleteNode(node,x)
        
    return t


