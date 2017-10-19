

def isListPalindrome(l):
    
    
    ln = 0
    n = l
    while n:
        ln += 1
        n = n.next

    #break the list

    if (not l) or (ln <=0) :
        return True

    n = l
    cnt = 0
    head2 = None
    while n:
        if cnt == ln/2:
            head2 = n
            break
        cnt += 1
        n = n.next


    #reverse head2

    



