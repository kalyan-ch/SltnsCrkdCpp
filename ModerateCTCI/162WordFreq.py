#single query O(n)
def getFreq(text,word):
	arr = text.split(" ")
	cnt = 0
	for x in arr:
		if x == word:
			cnt += 1

	return cnt

#multiple queries O(1) time and O(n) space

freqDc = {}
def initFreq(text):
	arr = text.split(" ")
	for x in arr:
		num = freqDc.get(x,0)
		num += 1
		freqDc[x] = num

def getFreq(text,word):
	if word not in text:
		return 0
	
	return freqDc[word]

