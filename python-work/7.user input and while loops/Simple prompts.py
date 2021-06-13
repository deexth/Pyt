#A simple prompt program
message = input("Tell me somthing, and i will repeat it to you: ")
print(message)

print("\n")
#now a greeter
name = input("Please enter your name: ")
print(f"\nHello, {name}")

#Using a variable as a prompt
prompt = "If you tell us who you are, we can personilize the messages you see."
prompt += "\nWhat is your first name: "
"""Putting the + before the equal sign tells pyython that the new string will be added to
the value of the variable prompt. Make sure to put a space between the prompt and the +"""
name = input(prompt)
if name != name.title():
    print(f"\nHello, {name.title()}")
else:
    print(f"\nHello, {name}")

#now let try some numbers
number = input("Enter a number and i'll tell you if its odd or even: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number}, is even.")
else:
    print(f"The number {number}, is odd.")
