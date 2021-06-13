#combining two programs pg205

import json

#load the username, if it has been stored previously
#otherwise, prompt for the username andstore it.

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
        
except FileNotFoundError:
    with open(filename, 'w') as f:
        username = input("Please enter your name: ")
        json.dump(username, f)
        
    print(f"We shall remember you next time, {username.title()}")
else:
    print(f"Welcome back, {username.title()}")