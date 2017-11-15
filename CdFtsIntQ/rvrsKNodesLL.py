# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    n = 0
    p = l
    
    while p:
        n += 1
        p = p.next
    
    #three pointers to iteratively reverse a list
    curr = l
    nxt = None
    prv = None
    count = 0

    #reversing only if number of nodes left is at least as much as k
    if n >= k:
        #reversing k nodes at once        
        while (curr and count < k):
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt
            count += 1

    if nxt:
        #recursively retrieving the nodes for next k reversed nodes
        l.next = reverseNodesInKGroups(nxt,k)
    else:
        #if nxt is none and prv is not none then length of list is multiple of k
        if prv:
            return prv

        #else just return the head of the remaining nodes
        return l
    
    
    return prv
