class House:
    
	def __init__(self, price):
		self.__price = 200

	@property
	def price(self):
		return self.price
	
	#@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	#@price.deleter
	def price(self):
		del self._price
  
  
house = House(50000.0) # Create instance

house.__price=100
print(house.__price)

