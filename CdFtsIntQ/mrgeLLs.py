# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def fillList(n1, n3):
    while n1:
        n3.next = ListNode(n1.value)
        n3 = n3.next
        n1 = n1.next


def mergeTwoLinkedLists(l1, l2):
    n1 = l1
    n2 = l2
    
    l3 = None
    n3 = l3
    
    if n1 and n2:
        num = 0
        if n1.value < n2.value:
            num = n1.value
            n1 = n1.next
        else:
            num = n2.value
            n2 = n2.next
    
        l3 = ListNode(num)
        n3 = l3
        
        while n1 and n2:
            nu = 0
            if n1.value <= n2.value:
                nu = n1.value
                n1 = n1.next
            else:
                nu= n2.value
                n2 = n2.next
            
            n3.next = ListNode(nu)
            n3 = n3.next

        if n1:
            fillList(n1,n3)
        if n2:
            fillList(n2,n3)

    elif not n1 and not n2:
        return None
    else:
        if n1:
            l3 = ListNode(n1.value)
            n1 = n1.next
            n3 = l3
            fillList(n1,n3)
        if n2:
            l3 = ListNode(n2.value)
            n2 = n2.next
            n3 = l3
            fillList(n2,n3)


    return l3





