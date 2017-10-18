
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def removeKFromList(l, k):
    n = l
    while n:
        if n.next.value == k:
            pass
        n = n.next


if __name__ == '__main__':
    l = ListNode(10)
    print l.value