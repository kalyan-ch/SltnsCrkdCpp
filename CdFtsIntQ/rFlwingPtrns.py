def areFollowingPatterns(strings, patterns):
    n = len(strings)
    
    str_pat = {}
    pat_str = {}
    
    res = True
    
    for i in range(n):
        s,p = strings[i],patterns[i]
        sv = str_pat.get(s,"")
        pv = pat_str.get(p,"")
        
        if sv == "":
            str_pat[s] = p
        else:            
            if sv != p:
                res = False
        
        if pv == "":
            pat_str[p] = s
        else:
            if pv != s:
                res = False
        
        
    return res

