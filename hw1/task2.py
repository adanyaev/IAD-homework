max = 0

for i in range (1, 1000):
	k = 0
	n = i
	while n != 1:
		if n%2 == 0:
			n = n/2
			k += 1
		else:
			n = 3*n+1
			k += 1
	if k >= max:
		max = k
		res = i

print(res)
