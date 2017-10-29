def insertBits(n, a, b, k):
    num1 = k << a
    for x in range(a,b+1):
        mask = 1 << x
        n = n & ~mask
    
    return n ^ num1