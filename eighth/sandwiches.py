# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandiwch. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the 
# sandwich that's being ordered. Call the function three times, using a different 
# number of arguments each time
def make_sandwich(*ingredients):
    print("Making a sandwich with the ingredients:")
    for ingredient in ingredients:
        print(f"\t-{ingredient.title()}")
    
make_sandwich("ham","cheese","pepper","sausage")
make_sandwich("pepper","ham")
make_sandwich("cheese")