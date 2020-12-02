import csv

def minmax(data, name, mode):
	f = (lambda x,y: x > y) if mode == "max" else (lambda x,y: x < y)
	r = data[0]
	for i in data:
		if i[name] != '-200':
			if f(int(i[name]), int(r[name])):
				r = i
	return r

def medconc(data):
	l = []
	i = 0
	while i < len(data):
		date = data[i][0]
		m = 0
		h = 0
		while i < len(data) and data[i][0] == date:
			for j in range(2,15):
				if data[i][j] != '-200':
					m += float(data[i][j])
			m /= 13
			i += 1
			h += 1
		l.append([date, m/h])

	return max(l, key=lambda x: x[1]), min(l, key=lambda x: x[1])

with open('AirQualityUCI.csv') as file:
	data = []
	reader = csv.DictReader(file, delimiter=';')
	data = [row for row in reader]
	print(int(data[0]['NOx(GT)']))

print(minmax(data, 'NOx(GT)', "max"))


with open('AirQualityUCI.csv') as file:
	data = []
	reader = csv.reader(file, delimiter=';')
	next(reader)
	for row in reader:
		data.append(row)

print(medconc(data))