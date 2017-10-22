

class BTNode(object):
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		return "Value: "+str(self.value)

	def __unicode__(self):
		return u"Value: "+str(self.value)