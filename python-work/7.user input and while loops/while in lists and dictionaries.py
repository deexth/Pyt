#confirmed_users.py
#Lets start with users that need to be verified,
#and an empty list to hold the verified users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#now lets verfiy the users, then move the verified users to the empty list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying the user: {current_user.title()}")
    confirmed_users.append(current_user)

#now lets display the confirmed users\
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"\t{confirmed_user.title()}")

print("\n")
#pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

print("\n")
#mountain.py
responses = {}

#lets set a flag to indicate the polling is active
polling_active = True

while polling_active:
    name = input("Please enter your name: ")
    response = input("\nWhere would you like to visit: ")

#now lets store the key and value in the dictionary
    responses[name] = response

#find out if anyone else wants to answer else stop the polling
    repeat = input("Would you like to let another person answer? (Yes/ No)")
    if repeat.lower() == 'no':
        polling_active = False
    
#now the polling has stopped and people who took part are going to be displayed along with their data.
print("---Poll results---")
for name, place in responses.items():
    print(f"\t{name.title()} would like to visit {place.title()}")