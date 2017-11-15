import re
import string
s = "bcd"
s = re.sub("[aeiou]","",s)

dict1 = {}
cnt = 1
alpha = string.ascii_lowercase
for ch in alpha:
	dict1[ch] = cnt
	cnt += 1

buf = ""
for x in s:
	if x not in buf:
		buf+=x

#encoding
newStr = ""
for i in range(len(buf)):
	if i == len(buf)-1:
		num = dict1[buf[0]]+dict1[buf[i]]
	else:
		num = dict1[buf[i]]+dict1[buf[i+1]]
	if num > 26:
		num = num % 26
	newStr += alpha[num-1]

print newStr


