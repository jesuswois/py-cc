# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”

import json

favorite_number = input("What's your favorite number?: ")

with open("favorite_number.txt",'w') as file_object:
    json.dump(favorite_number, file_object)