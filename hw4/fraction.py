
class Fractions:

	def __init__(self, num, den):
		self.num = num
		self.den = den
		self.cut()

	@staticmethod
	def nod(a, b):
		a = abs(a)
		b = abs(b)
		min = a if a<b else b
		for i in range(min, 0, -1):
			if a%i == 0 and b%i == 0:
				return i

	@staticmethod
	def nok(a, b):
		a = abs(a)
		b = abs(b)
		nok = a if a>b else b
		while nok%a or nok%b:
			nok += 1
		return nok

	def cut(self):
		if self.num == 0:
			self.den = 1
			return self
		nod = Fractions.nod(self.num, self.den)
		self.num //= nod
		self.den //= nod
		return self

	def __add__(self, other):
		nok = Fractions.nok(self.den, other.den)
		return Fractions(self.num*(nok//self.den)+other.num*(nok//other.den), nok)
		
	def __sub__(self, other):
		nok = Fractions.nok(self.den, other.den)
		return Fractions(self.num*(nok//self.den)-other.num*(nok//other.den), nok)

	def __mul__(self, other):
	 	return Fractions(self.num*other.num, self.den*other.den)

	def __truediv__(self, other):
		return Fractions(self.num*other.den, self.den*other.num)

	def __bool__(self):
		return True if self.num else False

	def __eq__(self, other):
		return False if self - other else True

	def __ne__(self, other):
		return True if self - other else False

	def __lt__(self, other):
		return True if (self-other).num < 0 else False

	def __le__(self, other):
		return True if (self-other).num <= 0 else False

	def __gt__(self, other):
		return True if (self-other).num > 0 else False

	def __ge__(self, other):
		return True if (self-other).num >= 0 else False

	def __str__(self):
		if self.num == 0:
			return "0"
		elif abs(self.num) == self.den:
			return str(self.num//abs(self.num))
		else:
			return "{}/{}".format(self.num, self.den)

	def __repr__(self):
		return str(self)


f1 = Fractions(-1,2)
f2 = Fractions(-3,4)
print(f1, f2)
print("{} + {} = {}".format(f1, f2, f1+f2))
print("{} * {} = {}".format(f1, f2, f1*f2))
print("{} - {} = {}".format(f1, f2, f1-f2))
print("{} - {} = {}".format(f2, f1, f2-f1))
print("{} == {} is {}".format(f1, f2, f1 == f2))
print("{} != {} is {}".format(f1, f2, f1 != f2))
print("{} < {} is {}".format(f1, f2, f1 < f2))
print("{} <= {} is {}".format(f1, f2, f1 <= f2))
print("{} > {} is {}".format(f1, f2, f1 > f2))
print("{} >= {} is {}".format(f1, f2, f1 >= f2))