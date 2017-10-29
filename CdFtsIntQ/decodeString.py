

def popStk(stk):
    temp = stk[-1]
    del stk[-1]
    return temp

def decodeString(s):

    cntStk = []
    dcStk = []
    
    n = len(s)
    i = 0

    dec = ""

    while i < n:
        if s[i].isdigit():
            
            count = 0
            while s[i].isdigit():
                count = 10*count + int(s[i])
                i += 1

            cntStk.append(count)

        elif s[i]=="[":
            
            dcStk.append(dec)
            dec = ""
            i += 1

        elif s[i] == "]":
            
            num = popStk(cntStk)
            tmp = popStk(dcStk) + num*dec
            dec = tmp
            i += 1
        else:
            dec += s[i]
            i += 1
            
    return dec
