class Food():

    def __init__(self, desc, price):
        self.description = desc
        try:
            price = float(price)
        except:
            self.cost = 0.0
        else:
            self.cost = price

    def get_details(self):
        return str('The %s will cost %.2f.' % (self.description, self.cost))

class Pizza(Food):
	
	def __init__(self,desc,price,*topping):
		Food.__init__(self,desc,price)
		self.toppings = topping

	
	def get_details(self):
		return str('The %s will cost %.2f. Toppings are: %s' % (self.description, self.cost, self.toppings))
		
george = Pizza("12' Pizza, thin base", 15.50, "Ham", "Cheese", "Pineapple")
luke = Pizza("5' Pizza thin", 9.95, "Cheese", "Tomato Base")
joan = Food("Sandwich", 4.50)
george = Pizza("18' Pizza, thin base", 15.50, "Ham", "Cheese", "Pineapple", "Tomato", "Beef", "Sausage", "Pepperoni", "Chilli Flakes")

print(george.get_details())
print(luke.get_details())
print(joan.get_details())
