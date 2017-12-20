from random import randint

class Box(object):
	def __init__(self, w,h,d):
		self.w = w
		self.h = h
		self.d = d

	def __str__(self):
		return "Box: "+str(self.w)+" "+str(self.h)+" "+str(self.d)

	def __repr__(self):
		return "Box: "+str(self.w)+" "+str(self.h)+" "+str(self.d)

	def __unicode__(self):
		return u"Box: "+str(self.w)+" "+str(self.h)+" "+str(self.d)

	def canAbove(self,box):
		if self.w < box.w and self.h < box.h and self.d < box.d :
			return True
		
		return False

		
def boxComp(b1,b2):
	return b2.h-b1.h

def crtStk(boxes):
	boxes.sort(boxComp)
	maxh = 0
	for x in range(len(boxes)):
		ht = stckNxt(boxes,x)
		maxh = max(maxh,h)

	return maxh

def stckNxt(boxes,i):
	bxbtm = boxes[i]
	maxh = 0
	for x in range(i+1,len(boxes)):
		if boxes[x].canAbove(bxbtm):
			h = stckNxt(boxes,x)
			maxh = max(maxh,h)

	maxh += bxbtm.h
	return maxh


if __name__ == '__main__':
	boxes = []
	for x in range(10):
		w = randint(1,30)
		h = randint(1,30)
		d = randint(1,30)
		boxes.append(Box(w,h,d))

	print crtStk(boxes)

