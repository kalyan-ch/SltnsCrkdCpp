def getPrimes(number):
    factors_list = []
    i = 2
    while number>1:     
        while number%i == 0:
            factors_list.append(i)
            number/=i
        i+=1
    
    return factors_list

def simplifyRational(num, den):
    if num == 0:
        return [0,1]

    f1 = getPrimes(abs(num))
    f2 = getPrimes(abs(den))
    
    nd = {}
    dd = {}

    for x in f1:
        num1 = nd.get(x,0)
        num1 += 1
        nd[x] = num1
    
    for x in f2:
        num1 = dd.get(x,0)
        num1 += 1
        dd[x] = num1
    
    for x in f1:
        num1 = dd.get(x,0)
        if num1 != 0:
            dd[x] -= 1

    dens = 1
    for x in dd:
        if dd[x]!=0:
            dens *= x*dd[x]

    for x in f2:
        num1 = nd.get(x,0)
        if num1 != 0:
            nd[x] -= 1

    nums = 1
    for x in nd:
        if nd[x]!=0:
            nums *= x*nd[x]
    

    if (num < 0 and den > 0) or (num > 0 and den < 0):
        nums *=  -1

    return [nums,dens]

if __name__ == '__main__':
    print simplifyRational(-90,24)
    
    
    