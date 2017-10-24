#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def kthSmallestInBST(t, k):
    count = 1
    n = t
    while n:
        if n.left:
            #find the right most leaf node of n.left node
            pre = n.left

            while pre.right and pre.right!=n:
                pre = pre.right

            #once the predecessor is found, link it to the root
            if not pre.right:
                pre.right = n
                n = n.left
            #if already linked to root and visiting again, remove the link
            else:
                pre.right = None
                if count == k:
                    break
                count += 1
                n = n.right

        else:
            #If no left child, visit the current node
            if count == k:
                break
            count += 1
            #then go to right branch
            n = n.right

    print "outside", n.value

    return n.value
