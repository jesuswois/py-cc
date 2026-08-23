""" Class used to represent a Restaurant """
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
