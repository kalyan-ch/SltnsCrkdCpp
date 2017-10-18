
def removeKFromList(l, k):
    if not l:
        return None
    
    if l.value == k:
        l = l.next
    
    
    if not l.next:
        if n.value == k:
            n = n.next
        
        return n
    
    while n.next:
        if n.next.value == k:
            n.next = n.next.next
        else:
            n = n.next

    return l
    
