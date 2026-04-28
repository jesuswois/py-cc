# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
import math

animals = ["hippo","lion","giraffe"]

for animal in animals:
    print("A "+animal+" wouldn't be a common pet!")

print("\nNone of those animals would be a common pet!")

animals.append("hyena")
animals.append("wolf")

# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
print("\nThe first three items in the list area: ")
print(animals[:3])

# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
print("\nThe three items from the middle of the list are: ")
print(animals[math.floor(len(animals)/2):math.floor(len(animals)/2)+3])

# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.
print("\nThe last three items from the list are: ")
print(animals[len(animals)-3:])


