# 10-12. Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.

import json

favorite_number = input("What's your favorite number?: ")

with open("favorite_number.txt",'w') as file_object:
    json.dump(favorite_number, file_object)

def get_stored_favorite_number():
    try:
        with open("favorite_number.txt") as file_object:
            favorite_number = json.load(file_object)
            print(f"I know your favorite number! It's {favorite_number}.")
    except FileNotFoundError:
        pass

