# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
buffet = ("scrambled eggs","waffles","sandwich","bread","hotcakes")
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
print("Our menu currently consists of:")
for food in buffet:
    print("\t-"+food.title())

# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.
buffet = ("cookies","apples","sandwich","bread","hotcakes")
print("Our menu has changed, now it consists of:")
for food in buffet:
    print("\t-"+food.title())