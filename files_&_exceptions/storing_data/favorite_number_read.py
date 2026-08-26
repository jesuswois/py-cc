# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”

import json

try:
    with open("favorite_number.txt") as file_object:
        favorite_number = json.load(file_object)
        print(f"I know your favorite number! It's {favorite_number}.")
except FileNotFoundError:
    pass