# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
#Recursive 


class Result(object):
	
	def __init__(self, node, result):
		self.node = node
		self.result = result
		

def isListPalindrome(l):
    lnth = 0
    n = l
    while n:
        lnth+=1
        n = n.next
    
    return isPalRecurse(l, lnth)
    
    
def isPalRecurse(nd, lnth):

	if (not nd) or (lnth <= 0):
		r = Result(nd, True)
		return r
	elif lnth == 1:
		r = Result(nd.next,True)
		return r

	res = isPalRecurse(nd.next, ln-2)

	if (not res.result) || (not res.node):
		return res


	res.result = (head.value == res.node.value)

	res.node = res.node.next;

	return res

