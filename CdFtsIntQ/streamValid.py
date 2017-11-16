def isNByte(n):
    i = 7
    count = 0
    while True:
        if i < 0:
            break
        mask = 1 << i        
        
        if n & mask == 0:
            break
        i -= 1
        count += 1
    
    return count

def isOneZero(n):
    mask = 1 << 7
    if n & mask == 0:
        return False
    
    mask = 1 << 6
    if n & mask != 0:
        return False
    
    return True

def streamValidation(stream):
    first = stream[0]
    n = isNByte(first)
    
    if n == 8:
        return False

    mask = 1 << 8-n-1
    
    if first & mask != 0:
        return False
        
    if n < len(stream):
        return False
        
    for i in range(1,n):
        if not isOneZero(stream[i]):
            return False
    
    return True