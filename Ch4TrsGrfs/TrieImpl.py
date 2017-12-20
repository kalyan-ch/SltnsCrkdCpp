class TrieNode(object):
	def __init__(self, val):
		self.val = val
		self.chldrn = {}
		self.prtl = ""
		self.word = ""

	def addChild(self,ltr,prtl):
		self.chldrn[ltr] = TrieNode(ltr)
		self.prtl = prtl


		