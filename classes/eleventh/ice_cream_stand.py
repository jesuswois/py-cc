# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant . Write 
# a class called IceCreamStand that inherits from the Restaurant class you wrote 
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of 
# the class will work; just pick the one you like better . Add an attribute called 
# flavors that stores a list of ice cream flavors . Write a method that displays 
# these flavors . Create an instance of IceCreamStand, and call this method 

class Restaurant:
    """
        Class specified in the exercise
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}, with a cuisine type of {self.cuisine_type}")

    def open_restaurent(self):
        print(f"The restaurant {self.restaurant_name} it's open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors = []):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("The Ice Cream Stand's flavors are:")
        for flavor in self.flavors:
            print(f"\t-{flavor.title()}")

restaurant = Restaurant("the mariachis","mexican")
restaurant.describe_restaurant()
restaurant.open_restaurent()

print()

icecreamstand = IceCreamStand("Ice Creams","italian",["chocolate","vanilla","strawberry","lemon","mango"])
icecreamstand.display_flavors()
