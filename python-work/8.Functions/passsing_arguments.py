#pets.py, POSITIONAL ARGUMENTS
print("POSITIONAL ARGUMENTS:")

def describe_pets(animal_type, pet_name):
    """Display info about a pet"""
    print(f"\tI have a {animal_type.title()}")
    print(f"\tMy {animal_type.title()}'s name is {pet_name.title()}.")

describe_pets('Hamster', 'Harry')

#Mutliple function calls, means we call call the function describe_pets endlessly
describe_pets('dog', 'chick')
"""Make sure while making a function call to put the arguments in the same positions as their parameters
otherwise it can be messy."""

#KEYWORD ARGUMENTS, pets.py
print("\n KEYWORD ARGUMENTS:")

def describe_pets(animal_type, pet_name):
    """Display info about a pet"""
    print(f"\tI have a {animal_type.title()}")
    print(f"\tMy {animal_type.title()}'s name is {pet_name.title()}.")

describe_pets(animal_type = 'Hamster', pet_name = 'Harry')
"""Now we are using keyword arguments which means that it does not matter in which order you put the
arguments since during the function call you assign the parameters to the arguments."""

#DEFAULT VALUES + EQUIVALENT FUNCTION CALLS, pets.py
print("\n DEFAULT VALUES:")

def describe_pets(pet_name, animal_type = 'dog'):
    """Display info about a pet"""
    print(f"\tI have a {animal_type.title()}")
    print(f"\tMy {animal_type.title()}'s name is {pet_name.title()}.")

describe_pets(pet_name = 'Harry')
#You can always call the function without using the keyword argument, e.g.
describe_pets('Harry')
#it doesn't mean that since a default value for animal_type was provided you can't still provide
#another type of the animal, i.e,
describe_pets(pet_name = 'Harry' ,animal_type = 'Hamster')
"""While using default values, the name-value of the function must be defined after the name-value
without the default argument, otherwise you will get an error."""



