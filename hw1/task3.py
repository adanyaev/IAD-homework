from random import randint as r
min = 1
print("Верхняя граница")
max = int(input())
n = r(1, max)
print("Число от {} до {}".format(min, max))
guess = int(input())
while guess != n:
	if guess > n:
		print("Нужно меньше")
		max = guess-1
	if guess < n:
		print("Нужно больше")
		min = guess+1
	print("Число от {} до {}".format(min, max))
	guess = int(input())
print("You won")

