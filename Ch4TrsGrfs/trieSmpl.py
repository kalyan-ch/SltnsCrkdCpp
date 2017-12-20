from TrieImpl import TrieNode

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

    def dfsGetWords(self,node,words):
        if node:
            for x in node.chldrn:
                self.dfsGetWords(node.chldrn[x],words)

            if node.word != "":
                words.append(node.word)
            

    def getWordsByPref(self,prfx):
        if prfx == None:
            return []
        cur = self.root
        words = []
        
        for ltr in prfx:
            if ltr in cur.chldrn:
                cur = cur.chldrn[ltr]
            else:
                return words

        self.dfsGetWords(cur,words)

        return words

    def getWords(self,part):
        que = {}
        collect(self,self.root,part,"","",0,que)
        return que

    def collect(self,node,part,"","",d,que):
        if not node:
            return



def findSub(words,parts):
    tr = Trie(TrieNode(""))

    for x in words:
        tr.insertInTrie(x)

if __name__ == '__main__':
    words = ["Apple", "Melon", "Orange", "Watermelon"]
    parts = ["a","mel","lon","el","An"]
    
    
    findSub(words,parts)


