"""Since the IF-ELIF-ELSE is strong, means it is used in case only one pass is needed. But what
if you need to check many other conditions before skiping to the next argumet."""
#we are going to use mutliple if to check if all aerguments are met before going to the last argument
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza.")
#from the above conditions it can be seen that only messages of items in the list will be printed