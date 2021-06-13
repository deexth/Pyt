#from time to time one might need to use an unkown number of arguments 
#hence an asterisk can be used in the parameter name
#pizza.py
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'yallopeno', 'brocolli')

print("\nAdd a message:")
#now lets make a list describing a pizza to be made

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'yallopeno', 'brocolli')

print("\nMixing positional and arbitrary arguments:")

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza(34,'pepperoni')
make_pizza(15,'mushrooms', 'yallopeno', 'brocolli')

print("\n\nUsing arbitrary keyword arguments.")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princenton', field='physics')

print(user_profile)

print("\n\nA more efficient way of using dictionaries in functions:")
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value
    """The for loop is to save the key-value elements."""
    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)