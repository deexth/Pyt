#In this program we will refactor the program remember_me.py
import json

file = 'user.json'

def get_stored_username():
    """This function will be retriving the username stored if available."""
    file = 'username.json'
    try:
        with open(file) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name?")
    with open(file, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name, accessing the 'greet_stored_username()'"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.title()}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}!")
        
greet_user()
