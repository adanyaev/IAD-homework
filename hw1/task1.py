
def count_words(txt):
	return txt.count(' ')+1
def top_ten(txt):
	words = txt.split(' ')
	for i in range(len(words)):
		words[i] = words[i].strip('.,!?;\'\"')
	rating = dict.fromkeys(set(words), 0)
	for i in words:
		rating[i] += 1
	d = []
	for i in range(10):
		m = 0
		for j in rating:
			if rating[j]>=m:
				m = rating[j]
				word = j
		d.append((word, m))
		rating.pop(word)
	return d
def reverse(txt):
	# txt.replace('!', '.')
	# txt.replace('?', '.')
	sentences = txt.split('.')
	for i in range(len(sentences)):
		sentences[i] = sentences[i].strip(' ')
	res = ''
	for i in sentences:
		words = i.split(' ')
		for i in range(len(words)):
			words[i] = words[i].strip('.,!?;\'\"')
		for i in range(len(words)-1, -1, -1):
			res += words[i]
			res += ' '
		res = res[0:len(res)-1] + '. '
	return res


txt = open("book.txt", 'r')
txt = txt.read()
print(count_words(txt))
print(top_ten(txt))
print(reverse(txt))

