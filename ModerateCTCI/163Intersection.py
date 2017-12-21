#write method to get intersection of two line segments

class Point(object):
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return str(self.x)+" "+str(self.y)

class Line(object):
	def __init__(self,p1,p2):
		if p1.x > p2.x :
			print p1,p2
			p1,p2 = self.swap(p1,p2)
			print p1,p2

		self.p1 = p1
		self.p2 = p2

		try:
			self.slope = (p1.y - p2.y)*1.0 / (p1.x - p2.x)
		except Exception as e:
			self.slope = "inf"
		
		if self.slope == "inf":
			self.yint = "inf"
			self.xint = p1.x
		else:
			self.yint = p1.y - self.slope * p1.x
			if self.slope == 0:
				self.xint = "inf"
			else:
				self.xint = (-1.0 * self.yint)/self.slope

	def swap(self,p1,p2):
		temp = p1
		p1 = p2
		p2 = temp
		return p1,p2

def getIntZero(line1,line2):
	y = line1.yint
	x = (y-line2.yint)/line2.slope
	return x,y

def getIntInf(line1,line2):
	x = line1.xint
	y = line2.slope*x+line2.yint
	return x,y

def isBetween(pt,line):
	if pt.x > line.p1.x and pt.x < line.p2.x:
		return True
	return False

		
def intersection(st1,en1,st2,en2):

	line1 = Line(st1,en1)
	line2 = Line(st2,en2)

	if line1.slope == line2.slope:
		pass
	elif line1.slope == 0:
		x,y = getIntZero(line1,line2)
	elif line2.slope == 0:
		x,y = getIntZero(line2,line1)
	elif line1.slope == "inf":
		x,y = getIntInf(line1,line2)
	elif line2.slope == "inf":
		x,y = getIntInf(line2,line1)
	else:
		x = (line1.yint - line2.yint )/(line2.slope - line1.slope)
		y = line1.slope*x + line1.yint

	intr = Point(x,y)
	print intr
	if isBetween(intr,line1) and isBetween(intr,line2):
		return intr
	return None

if __name__ == '__main__':
	st1 = Point(1,7)
	en1 = Point(0,5)
	st2 = Point(0,2)
	en2 = Point(3,5)
	print intersection(st1,en1,st2,en2)