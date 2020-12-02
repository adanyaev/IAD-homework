
def range_double(*args):
	if len(args) == 1:
		start = 0.0
		stop = args[0]
		step = 1.0
	elif len(args) == 2:
		start = args[0]
		stop = args[1]
		step = 1.0
	elif len(args) == 3:
		start = args[0]
		stop = args[1]
		step = args[2]
	else:
		raise TypeError
	res = []
	while start < stop:
		res.append(start)
		start += step
	return res

def range_time(*args):
	if len(args) == 1:
		start = [0,0,0]
		stop = args[0]
		step = [1,0,0]
	elif len(args) == 2:
		start = args[0]
		stop = args[1]
		step = [1,0,0]
	elif len(args) == 3:
		start = args[0]
		stop = args[1]
		step = args[2]
	else:
		raise TypeError

	res = []
	to_sec = lambda t: t[0]*3600 + t[1]*60 + t[2]
	while to_sec(start) < to_sec(stop):
		res.append(start)
		start = [start[i] + step[i] for i in range(3)]
		if start[2] >= 60:
			start[2] %= 60
			start[1] += 1
		if start[1] >= 60:
			start[1] %= 60
			start[0] += 1

	return res

print(range_double(0.0, 5.0, 0.1))
print(range_double(5.764, 8.634))
print(range_double(2.11, 5.576, 3.4))

print(range_time([2,10,0]))
print(range_time([2,10,0], [5, 0, 0]))
print(range_time([2,10,0], [4, 0, 0], [0, 15, 20]))





