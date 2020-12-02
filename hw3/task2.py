import os

def get_files(path):
	files = []
	for rpath, _ , names in os.walk(path):
		for i in names:
			files.append(rpath + '\\' + i)
	return files


print(get_files(r'D:\other\code\PyCode\IAD\hw3\test'))
