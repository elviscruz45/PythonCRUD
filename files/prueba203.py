
a="hola"

class Date:
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
	def __format__(self, code):
		if code == '':
			code = 'dmy'
		fmt =a 
		return fmt

e = Date(2012, 12, 21)
print(format(e))