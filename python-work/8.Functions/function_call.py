# greeter.py
# --strict
def greeter_user() -> None:
    """Display a simple greeting"""
    print("Hello!")


# Now lets add a parameter to greeter_user,
def greeter_user(username: str) -> None:
    """Display a simple greeting"""
    print(f"\nHello!, {username.titlet()}")


greeter_user(input())
"""The word 'username' in the parentheses of greeter_user is a parameter, means while calling
the function we will have to put an argument in the parentheses of greeter_user which is 'jesse' in this
case."""
