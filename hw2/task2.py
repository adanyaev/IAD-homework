def find_all_primes (n):
	list = []
	for i in range (2, n):
		f = True
		for j in range (2, i):
			if i%j == 0:
				f = False
		if f == True:
			list.append(i)
	return list


def find_dividers (n):
	list = []
	for i in range (1, n+1):
		if n%i == 0:
			list.append(i)
	return list


def find_nod (n1, n2):
	for i in range(1, min(n1, n2)+1):
		if n1%i == 0 and n2%i == 0:
			res = i
	return res


print(find_all_primes(20))
print(find_dividers(20))
print(find_nod(20, 10))



