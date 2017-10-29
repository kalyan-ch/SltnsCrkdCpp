stk = []

def pop():
    if stk:
        temp = stk[-1]
        del stk[-1]
        return temp

def simplifyPath(path):
    
    while path.find("//") > -1:
        path = path.replace("//","/")

    arr = path.split("/")
    
    arr[:]= [str(x) for x in arr if x != "." and x != ""]
    
    print arr        
    for i in range(len(arr)):
        if arr[i] == "..":
            pop()
        else:
            stk.append(arr[i])
    
    res = "/"
    res += "/".join(stk)
    
        
    return res
