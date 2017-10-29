
def popStack(stk):
    temp = stk[-1]
    del stk[-1]
    return temp

def nextLarger(a):
    n = len(a)
    res = [-1 for x in range(n)]
    stk = [a[0]]
    

    for i in range(1,n):
        if stk:
            curr = popStack(stk)
            nxt = a[i]

            while nxt > curr:
                res[a.index(curr)]=nxt
                if not stk:
                    break
                curr = popStack(stk)

            if nxt < curr:
                stk.append(curr)

        stk.append(nxt)

    while(stk):
        ele = popStack(stk)
        res[a.index(ele)] = -1
    
    return res

