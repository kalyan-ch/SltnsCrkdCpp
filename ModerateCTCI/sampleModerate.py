fives = 0
twos = 0

for i in range(1,6):
	x = i
	while x%5 == 0:
		fives += 1
		x = x/5
	
	y = i
	while y%2 == 0:
		twos += 1
		y = y/2


print min(fives, twos)

