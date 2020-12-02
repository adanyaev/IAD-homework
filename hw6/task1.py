import csv
import math
import numpy as np
import scipy.spatial.distance as ds

def distance(v1, v2):
	return math.sqrt(abs((v1[0]-v2[0]))**2 + abs((v1[1]-v2[1]))**2)

def get_top10(data, key):
	data1 = data[:]
	top10 = []
	for i in range(10):
		
		d = data1[0]
		for j in data1:
			if key(j) > key(d):
				
				d = j
		top10.append(d)
		data1.remove(d)
	return top10

with open('quake.csv') as file:
	data = []
	reader = csv.reader(file)
	next(reader)
	for row in reader:
		data.append([float(i) for i in row])
# c1 = 0
# for i in data:
# 	if i[3]>5:
# 		c1 += 1
# print(c1)

print(get_top10(data, lambda x: x[0]))
print(get_top10(data, lambda x: x[3]))

east = [i for i in data if i[2] > 0]
print(get_top10(east, lambda x: x[0]))
print(get_top10(east, lambda x: x[3]))

west = [i for i in data if i[2] < 0]
print(get_top10(west, lambda x: x[0]))
print(get_top10(west, lambda x: x[3]))

north = [i for i in data if i[1] > 0]
print(get_top10(north, lambda x: x[0]))
print(get_top10(north, lambda x: x[3]))

south = [i for i in data if i[1] < 0]
print(get_top10(south, lambda x: x[0]))
print(get_top10(south, lambda x: x[3]))

# v1, v2 = data[0], data[1]
# d = distance([data[0][1], data[0][2]], [data[1][1], data[1][2]])
# for i in range(len(data)):
# 	for j in range(i+1, len(data)):
# 		dis = distance([data[i][1], data[i][2]], [data[j][1], data[j][2]])
# 		if dis > d:
# 			d = dis
# 			v1, v2 = data[i], data[j]

# print(v1, v2, d)

# v1, v2 = data[0], data[1]
# d = ds.cosine([data[0][1], data[0][2]], [data[1][1], data[1][2]])
# for i in range(len(data)):
# 	for j in range(i+1, len(data)):
# 		dis = ds.cosine([data[i][1], data[i][2]], [data[j][1], data[j][2]])
# 		if dis > d:
# 			d = dis
# 			v1, v2 = data[i], data[j]

# print(v1, v2, d)






