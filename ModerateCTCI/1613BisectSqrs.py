
class Point(object):
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return str(self.x)+" "+str(self.y)

class Line(object):
	def __init__(self,slope,yint,xint):
		self.slope = slope
		self.yint = yint
		self.xint = xint
		

def bisectSquares(mid1,mid2):

	if mid1.x == mid2.x and mid1.y == mid2.y:
		return mid1

	if mid1.x == mid2.x:
		return Line("inf","inf",mid1.x)

	slope = (mid1.y - mid2.y)*1.0/(mid1.x - mid2.x)
	yint = mid1.y - slope * mid1.x
	xint = -1.0 * yint / slope

	res = Line(slope,yint,xint)
	return res

if __name__ == '__main__':
	print bisectSquares(Point(0,0),Point(2,2))