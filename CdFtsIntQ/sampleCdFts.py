def isNByte(n):
    i = 7
    count = 0
    while True:
        mask = 1 << i
        if n & mask == 0 or i == 0:
            break
        i -= 1
        count += 1
    
    return count


print isNByte(255)