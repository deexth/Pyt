#first example
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza.")
else: 
    print("Are you sure you want a plain pizza?")

""""Since the list is empty before python reaches the for loop the if condition is not cleared out 
hence the Else condition is executed."""

#second example
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

if available_toppings and requested_toppings: 
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"\tAdding {requested_topping}.")
        else:
            print(f"\tSorry, we don't have {requested_topping}.")
else:
    print("One of the lists is empty again.")
print("\nFinished making your pizza!") 

"""This program contains multiple lists, it can be compared to a daily life example; the requested_toppings
are the toppings ordered by the user, python's IF at point 21 will check whether the toppings ordered
are part of the available toppings if not the right message will be printed."""