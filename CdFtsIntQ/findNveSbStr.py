def findSubstrings(words, parts):
    res = []
    for w in words:
        match = ""
        lngst = 0
        pos = len(w)
        for p in parts:
            if p in w:

                if len(p) > lngst or (len(p) == lngst and w.index(p) < pos):
                    lngst = len(p)
                    pos = w.index(p)
                    match = p

        if lngst > 0:
            ind = w.index(match)
            res.append(w[0:ind]+"["+match+"]"+w[ind+len(match):])
        else:
            res.append(w)

    return res

if __name__ == '__main__':
    print findSubstrings(["Apple","Melon","Watermelon","Orange"],["a","mel","lon","el","An"])
