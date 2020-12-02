def transform (n, fr, to):
	n = str(n)
	n_10 = 0
	for i in range(len(n)):
		if 48 <= ord(n[i]) <= 57:
			c = ord(n[i])-48
		elif 65 <= ord(n[i]) <= 90:
			c = ord(n[i])-55
		n_10 += c*(fr**(len(n)-1-i))
	n_to = ''
	while n_10 >= to:
		c = n_10%to
		if c >= 10:
			c = chr(c+55)
		n_to += str(c)
		n_10 = n_10//to
	if n_10 >= 10:
		n_10 = chr(n_10+55)
	n_to += str(n_10)
	s = n_to[::-1]
	return s


print (transform('ABC420EA', 20, 7))



