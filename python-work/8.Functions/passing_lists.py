# greeter.py
def greet_users(names: list[str]) -> None:
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ["hannah", "ty", "mrgot"]
greet_users(usernames)

print("\n")
print("\nModifying a list in a function:")


# printing_models.py,
# modifying a list in a function
# start with some designs that need to be printed
def print_models(unprinted_designs: list[str], completed_designs: list[str]) -> None:
    """Simulate printing each design, until none are left
    move each design to completed_designs after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design.title()}")
        completed_designs.append(current_design)


def show_completed(completed_designs: list[str]) -> None:
    """Show all models that were printed."""
    print("\nThe following models have been printed:")

    for completed_design in completed_designs:
        print(f"\t- {completed_design.title()}")


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_designs = []

print_models(unprinted_designs[:], completed_designs)
show_completed(completed_designs)

print("\n")
print("\nPreventing a function from modifying a list:")
"""from preventing to lose data of a list you can use a copy by using this line of code
i.e. function_name(list_name[:])"""

print(unprinted_designs)
