# 8-17. Styling Functions: Choose any three programs you wrote for this chapter,
# and make sure they follow the styling guidelines described in this section.
def make_sandwich(*ingredients):
    """ 
        Prints the ingredients for the sandwich that's being made
    """
    print("Making a sandwich with the ingredients:")
    for ingredient in ingredients:
        print(f"\t-{ingredient.title()}")

make_sandwich("ham","cheese","pepper","sausage")
make_sandwich("pepper","ham")
make_sandwich("cheese")