# 10-13. Verify User: The final listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the person who
# last used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not, call get_new_username() to get the correct
# username.

import json

def get_stored_username():
    """Tries to retrieve a stored username"""
    try:
        with open('username.txt') as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else: 
        return username

def get_new_username():
    """Prompts for a username"""
    input_username = input("Enter your username: ")
    with open('username.txt','w') as file_object:
        username = json.dump(input_username,file_object)
        return input_username

def greet_user():
    """Greets user if stored, otherwise if not stored or if user indicates the name is not his, then
    prompts for a new username"""
    username = get_stored_username()
    if username:
        is_user_correct = input(f"Is your username {username}? (Y/N): ")
        if is_user_correct == 'Y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"I'll remember you next time, {username}.")
    else:
        username = get_new_username()
        print(f"I'll remember you next time, {username}.")

greet_user()
