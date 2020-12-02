import random

def flip(chance):
	if random.random() < chance:
		return 1
	else:
		return 0

def flips(chance, num1, num2=1):
	l = [0 for i in range (num1)]
	for i in range(num1):
		for j in range(num2):
			l[i] += (flip(chance))
	return l



a = flips(0.5, 1, 5)
print (a)

