# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
# that do each of the following at least once:
# •	Use a conditional test in the while statement to stop the loop .
# •	Use an active variable to control how long the loop runs .
# •	Use a break statement to exit the loop when the user enters a 'quit' value

def add_topping(topping):
    print("I'll add "+topping+" to your pizza!\n")

prompt = "Please enter the topping you'd like: "
topping = ""
max_toppings = 5
accumulated_toppings = 0

while topping != "quit":
    topping = input(prompt)
    
    if topping=="quit":
        print("Exiting program...")
        break;
    elif accumulated_toppings==5:
        print("Topping's maximum cantity reached, exiting...")
    
    add_topping(topping)
    accumulated_toppings += 1