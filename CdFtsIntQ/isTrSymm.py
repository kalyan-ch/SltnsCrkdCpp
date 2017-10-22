#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
arr = []

def inorder(node):
    if node:        
        inorder(node.left)
        arr.append(node.value)
        inorder(node.right)

def isTreeSymmetric(t):
    if (not t.left) or (not t.right):
        return False
    elif not t:
        return True

    inorder(t)
    
    n = len(arr)

    for x in range(n/2):
        if arr[i] != arr[n-1-i]:
            return False

    return True
    

