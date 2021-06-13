#greeter.py
def greeter_user():
    """Display a simple greeting"""
    print("Hello!")

greeter_user()
"""The 'def' before greeter_user is to tell python that we are defining the function
greeter_user"""

#Now lets add a parameter to greeter_user,
def greeter_user(username):
    """Display a simple greeting"""
    print(f"\nHello!, {username.title()}")

greeter_user('jesse')
"""The word 'username' in the parentheses of greeter_user is a parameter, means while calling
the function we will have to put an argument in the parentheses of greeter_user which is 'jesse' in this
case."""