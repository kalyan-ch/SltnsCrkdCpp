def multiply(pos):
    if not pos:
        return []
    
    if len(pos) == 1:
        return list(pos[0])

    res = []
    rem = multiply(pos[1:])
    s1 = pos[0]
    for x in s1:        
        res.extend([x+y for y in rem])
    
    return res

def pressingButtons(buttons):
    data = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    pos = [data[int(x)] for x in buttons]
    res = multiply(pos)
    return res

