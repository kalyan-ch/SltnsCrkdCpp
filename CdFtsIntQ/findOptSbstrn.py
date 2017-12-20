

class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.chldrn = {}
        self.prtl = ""
        self.word = ""

    def addChild(self,ltr,prtl):
        self.chldrn[ltr] = TrieNode(ltr)
        self.prtl = prtl

class Trie(object):
    def __init__(self, root):
        self.root = root


    def insertInTrie(self,word):
        cur = self.root
        isInstd = True
        j = 0
        for i in range(len(word)):
            if word[i] in cur.chldrn:           
                cur = cur.chldrn[word[i]]
            else:
                j = i
                isInstd = False
                break

        if not isInstd:
            while j < len(word):
                prtl = word[0:j]
                cur.addChild(word[j],prtl)
                cur = cur.chldrn[word[j]]
                j += 1

        cur.word = word
        cur.prtl = word

    def isInTrie(self,stri):
        cur = self.root
        for x in stri:
            if x in cur.chldrn:
                cur = cur.chldrn[x]
            else:
                return False

        if cur.word != "" and cur.word == stri:
            return True
        else:
            return False

def findSubInWord(w,root):
    lngst = 0
    lngstPos = 0
    for i in range(len(w)):
        cur = root
        for pos in range(i,len(w)):
            ltr = w[pos]
            if ltr not in cur.chldrn:
                break
            cur = cur.chldrn[ltr]
            ln = pos - i + 1
            if cur.word != "" and ln > lngst:
                lngst = ln
                lngstPos = i

    if lngst > 0:
        final = w[0:lngstPos]+"["+w[lngstPos:lngst+lngstPos]+"]"+w[lngst+lngstPos:]
        return final
    else:
        return w
        


def findSubStrings(words,parts):
    res = []
    #create a trie with parts strings
    tr = Trie(TrieNode(""))

    for p in parts:
        tr.insertInTrie(p)

    for w in words:
        res.append(findSubInWord(w,tr.root))

    return res

if __name__ == '__main__':
    
    words = ["Apple", "Melon", "Orange", "Watermelon"]
    parts = ["a", "mel", "lon", "el", "An"]

    print findSubStrings(words,parts)
