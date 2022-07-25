class House:
    
	def __init__(self, price):
		self.__price = price

	@property
	def price(self):
		return self.__price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self.__price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self.__price
  

house = House(50000.0)  # Create instance
house.price = 45000.0   # Update value
print(house.price)             # Access value
