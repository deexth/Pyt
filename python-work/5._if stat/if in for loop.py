#now using the if statement in the for loop
requested_toppings = ['mushrooms','green peppers','extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"We are out of {requested_topping}")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza.")
"""first python will loop in the list, if the requested topping is not available at ,point 5, then
a message will be printed to let the user know that that topping is finished"""