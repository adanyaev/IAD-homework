
def permutations(s, l, repeat=True):
	for i in s:
		if l != 1:
			if repeat:
				sn = s
			else:
				sn = list(s)
				sn.remove(i)
				if len(sn) == 0:
					raise ValueError("More symbols are required in the input string")
			for j in permutations(sn, l-1, repeat):
				yield (i, ) + j
		else:
			yield (i, )


def perstr(s):
	return list(set(["".join(i) for i in permutations(s, len(s), False)]))


print(next(permutations('abc', 2, False)))
print(next(permutations('abc', 5, True)))
#print(next(permutations('abc', 5, False)))
print(next(permutations('aab', 2, False)))


print(perstr("aab"))

