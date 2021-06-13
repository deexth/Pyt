#counting.py 
current_number = 1

while current_number <=5:
    print(current_number)
    current_number += 1
"""The program will run till current_number is equal to 5."""

#parrot.py with a quit twist
prompt = "If you tell us who you are, we can personilize the messages you see."
prompt += "\nEnter 'quit' to exit the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
"""The program wil run till 'quit' is entered, The 'message = input(prompt)' can not be put above the
while condition otherwise the program program will become an infinite loop in case 'quit'
is not entered on the first trial."""

#now from the above program lets make some changes so that quit is not displayed
print("\n")
print("Parrot.py second run")
prompt = "\tIf you tell us who you are, we can personilize the messages you see."
prompt += "\n\tEnter 'quit' to exit the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        if message != message.title():
            print(f"\t{message.title()}")
        elif message == message.title():
            print(f"\t{message}")

"""Now in this following program we will initialize a new vaiable lets call it active,
Python will check if active is still true to continue running the program."""
print("\n")
prompt = "If you tell us who you are, we can personilize the messages you see."
prompt += "\nEnter 'quit' to exit the program: "
#variables like active are what is called flags in python.
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#cities.py, lets now try new things like break.
print("\n")

prompt = "Please enter the name of a city you have visited."
prompt += "\nEnter 'quit' to exit the program: "
#variables like active are what is called flags in python.

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"I would like to visit {message.title()}")
"""When message becomes quit python will stop the program and the rest of the program 
will not be compiled."""

#Continue, now lets use continue for a change in #counting.py
print("\n")

current_number = 0

while current_number <10: #if current_number is <11, 11 will also be outputed.
    current_number += 1

    if current_number % 2 == 0:
        continue

    print(current_number)
"""Python will check if the current number is not divisible by 2, if it is then python will
skip the rest of the program and go to the start again till all number in the range 0 to 11 are all done."""
