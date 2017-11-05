def getPerms(s):
    
    if len(s) == 1:
        return [s]

    if len(s) == 2:
        return [s[0]+s[1],s[1]+s[0]]
        
    rem = getPerms(s[1:])
    fst = s[0]
    
    res = []

    for x in rem:
        res.extend(fst+x)

    return res

def stringPermutations(s):
    res = getPerms(s)
    return res
    
if __name__ == '__main__':
    print stringPermutations("ABA")
