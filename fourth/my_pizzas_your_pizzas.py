# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.

pizzas = ["shrimp","pepperoni","hawaiian"]

friend_pizzas = pizzas[:]

# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. 
pizzas.append("mushroom")
friend_pizzas.append("extra cheese")

# Print the message, 
# My favorite pizzas are:, 
# and then use a for loop to print the first list. 
print("My favorites pizzas are:")
for pizza in pizzas:
    print("\t-"+pizza.title()+" pizza.")

# Print the message,
# My friend’s favorite pizzas are:, 
# and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("\t-"+pizza.title()+" pizza.")