#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def isEqual(r1,r2):
    if r1 and r2:
        if ((r1.value == r2.value) and isEqual(r1.left,r2.left) and isEqual(r1.right,r2.right)):
            return True
    elif (not r1) and (not r2):
        return True
    else:
        return False


def isSubtree(t1, t2):

    if t2:
        if t1:
            this_level = [t1]
            count = 0
            while this_level:
                next_level = []
                for node in this_level:
                    
                    if node.value == t2.value:
                        if isEqual(node,t2):
                            count = 1
                            break
                    
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                
                if count == 1:
                    break
                
                this_level = next_level
                
            if count == 1:
                return True
            return False
        
        else:
            return False
    else:
        return True
        

