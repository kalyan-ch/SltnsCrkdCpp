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
    rn = len(res)/4 + len(res)%4

    for x in range(rn)[::-1]:
        end = 4*(i-1)+1
        start = 4*(i-2)+1

        if i == 0:
            pass
        else:
            arr.append(int(res[start:end]))


    print res,arr




    r = ListNode(int(arr[0]))
    
    for x in arr[1:]:
        if x!= "":
            node = ListNode(int(x))
            n = r
            while True:
                if not n.next:
                    n.next = node
                    break

                n = n.next


    return r
