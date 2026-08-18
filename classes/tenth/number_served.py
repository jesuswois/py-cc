# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166) . 
# Add an attribute called number_served with a default value of 0 . Create an 
# instance called restaurant from this class . Print the number of customers the 
# restaurant has served, and then change this value and print it again .
# Add a method called set_number_served() that lets you set the number 
# of customers that have been served . Call this method with a new number and 
# print the value again .
# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served . Call this method with any num
# ber you like that could represent how many customers were served in, say, a 
# day of business 

class Restaurant:
    """
        Class specified in the exercise
    """
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}, with a cuisine type of {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} it's open!\n")

    def get_number_served(self):
        print(f"The restaurant has served {self.number_served} customers.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

restaurant = Restaurant("the mariachis","mexican")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("la francesa","french",10)
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
# Printing initial number of customers served
restaurant2.get_number_served()

# Changing the number of customers served
restaurant2.number_served = 20
restaurant2.get_number_served()

# Changing the number of costumers served using a method
restaurant2.set_number_served(30)
restaurant2.get_number_served()

# Incrementing the number of costumers served using a method
restaurant2.increment_number_served(15)
restaurant2.get_number_served()