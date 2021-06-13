#The keys() statement which is used in order to output the key of a dictionary
favorite_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in favorite_lang.keys():
    print(name.title())

"""The keys statement is the default output value of a dictionary in loop, it means that the statement
:FOR NAME IN favorite_lang.KEYS() is the same as FOR NAME IN favorite_lang it would give the same output."""
#e.g.
print("\n")
for name in favorite_lang:
    print(name.title())

print("\n")
#Now lets use KEYS() with messages

friends = ['phil', 'sarah']
for name in favorite_lang.keys():
    print(f"Hi {name.title()}")
    
    if name in friends:
        lang = favorite_lang[name].title()
        print(f"\t{name.title()}, I see you love {lang}")

print("\n")
"""The KEYS() statement can also be used to find out if a particular person was polled"""
if 'erin' not in favorite_lang.keys():
    print("Erin, please take our poll.")

print("\n")
#Now lets sort the keys in the dictionary
for name in sorted(favorite_lang.keys()):
    print(f"{name.title()}, thank you for taking the poll.")