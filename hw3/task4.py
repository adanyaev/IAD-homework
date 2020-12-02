def enum(c, start=0):
    ret = []
    for i in c:
        ret.append((start, i))
        start += 1
    return iter(ret)


for i in enum([1,2,3,4,5]):
	print (i)
