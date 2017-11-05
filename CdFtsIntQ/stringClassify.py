def vowCheck(s,ind):

    #xx?

    #?xx
    #x?x
    pass

def consCheck(s,ind):

    pass

def classifyStrings(s):
    
    vow = ["a","e","i","o","u"]
    cons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    
    v_cnt = 0
    c_cnt = 0
    res = "good"
    lis = []
    for i in range(len(s)):
            
            if s[i] in vow:
                v_cnt += 1  
                c_cnt = 0
            else:
                if s[i] in cons:
                    c_cnt += 1
                    v_cnt = 0
                    
            if v_cnt == 3:
                lis.append(0)
            if c_cnt == 5:
                lis.append(1)


    ind = s.find("?")

    vowCheck(s,ind)
    consCheck(s,ind)

    if lis:
        res = "bad"
    
    return res

            
