# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def getNum(head):
    p1 = head
    n1 = "" 
    while p1:
        num = str(p1.value)
        n = len(num)
        if n < 4:
            x = ["0" for x in range(n,4)]
            st = "".join(x)
            num = st+num

        n1 += str(num)
        p1 = p1.next

    return int(n1)


def addTwoHugeNumbers(a, b):
    n1 = getNum(a)
    n2 = getNum(b)

    result = n1+n2
    res = str(result)

    arr = []
    n = len(res)

    for x in xrange(n,-1,-4):
        end = x
        start = x-4
        
        if start < 0:
            start = 0
        if end > 0:
            num = res[start:end]
            arr.append(int(num))


    r = None
    
    for x in arr[::-1]:
        if r:
            node = ListNode(int(x))
            n = r
            while True:
                if not n.next:
                    n.next = node
                    break

                n = n.next
        else:
            r = ListNode(int(x))
        


    return r
