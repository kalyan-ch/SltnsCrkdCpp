#
# Definition for binary tree:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)+" Left: "+str(self.left)+" Right: "+str(self.right)


def buildFromInOrder(inorder, preorder, inS, inE, preS):
    if inE < inS or preS > len(preorder):
        return None

    num = preorder[preS]
    root = Tree(num)
    inInd = inorder.index(num)

    root.left = buildFromInOrder(inorder, preorder, inS, inInd-1, preS+1)
    root.right = buildFromInOrder(inorder, preorder, inInd+1, inE, preS+inInd-inS+1)
    return root


def restoreBinaryTree(inorder, preorder):
    root = buildFromInOrder(inorder, preorder, 0, len(inorder)-1, 0)
    return root


if __name__ == '__main__':
    inorder = [5,4,3,1]
    preorder = [1,3,4,5]
    root = restoreBinaryTree(inorder,preorder)
    print root
