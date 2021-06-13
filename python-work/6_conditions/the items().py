#In case there is need to return a dictionary in a loop we use the items() function
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

"""During the declaration the variable names for the key-value can be named anything, it does not
necessary mean it has to be named KEY and VALUE"""

print("\n")
#Another example of looping through a dictionary
favorite_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_lang.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

"""In this previous example the variable have been named name and language in order to make 
more sense."""    