from random import randint as r
max = 0
min = 1
print("Верхняя граница")
max = int(input())
print("Загадайте число от {} до {}".format(min, max))
guess = r(min, max)
print(guess)
ans = input()
while ans != "=":
	if ans == "<":
		max = guess-1
	if ans == ">":
		min = guess+1
	print("Число от {} до {}".format(min, max))
	guess = r(min, max)
	print(guess)
	ans = input()
print("Good game!")

