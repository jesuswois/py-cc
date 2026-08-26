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
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"I'll remember you next time, {username}.")

greet_user()
