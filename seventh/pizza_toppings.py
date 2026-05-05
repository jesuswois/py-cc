# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value . As they enter each topping, 
# print a message saying you’ll add that topping to their pizza .
def add_topping(topping):
    print("I'll add "+topping+" to your pizza!\n")

prompt = "Please enter the topping you'd like: "
topping = ""

while topping != "quit":
    topping = input(prompt)
    if topping!="quit":
        add_topping(topping)
    else:
        print("Exiting program...")

