ones = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
hndrd = "Hundred"
neg = "Negative"
lrg = ["","Thousand","Million","Billion","Trillion"]

def cnvCnk(n):
	prts = []
	if n >= 100:
		prts.append(ones[n/100])
		prts.append(hndrd)
		n = n%100
	
	if n >= 10 and n <=19:
		prts.append(ones[n])
	elif n >= 20:
		prts.append(tens[n/10])
		n %= 10

	if n >= 1 and n <= 9:
		prts.append(ones[n])

	return " ".join(prts)

def numInWords(num):
	
	if num == 0:
		return ones[0]
	elif num < 0:
		return neg+" "+numInWords(-1*num)

	parts = []
	cnt = 0

	while num > 0:
		if num % 1000 != 0:
			cnk = cnvCnk(num%1000) + " " + lrg[cnt]
			parts.append(cnk)
		num /= 1000
		cnt += 1

	return " ".join(parts[::-1])



if __name__ == '__main__':
	print numInWords(-3000000)