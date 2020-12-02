def strcmp(s1, s2):
	
	for i in range (min(len(s1), len(s2))):
		if ord(s1[i]) > ord(s2[i]):
			return 1
		elif ord(s1[i]) < ord(s2[i]):
			return -1
	if len(s1) > len(s2):
		return 1
	elif len(s1) < len(s2):
		return -1
	else:
		return 0


def listcmp(l1, l2):
	if len(l1) > len(l2):
		return 1
	elif len(l1) < len(l2):
		return -1
	for i in range (len(l1)):
		if type(l1[i]) is str and type(l2[i]) is str:
			if strcmp(l1[i], l2[i]) != 0:
				return strcmp(l1[i], l2[i])
		if type(l1[i]) is int and type(l2[i]) is int:
			if l1[i] != l2[i]:
				return (l1[i]-l2[i])/abs(l1[i]-l2[i])
		if type(l1[i]) != type(l2[i]):
			if type(l1[i]) is str:
				return 1
			else:
				return -1
	return 0

def find(cr, a):
	m = 1 if cr == 'max' else -1
	cmp = strcmp if a[0] is str else listcmp
	tmp = a[0]
	for i in a:
		if cmp(i, tmp) == m:
			tmp = i
	return tmp

print (find('min', [['sbd', 'rwas'], ['dsdsd', 'dsadarw']]))




				


