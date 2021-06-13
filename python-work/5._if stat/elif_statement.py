#Here we will use mutliple conditions
age = 12

if age < 4:
    price = 0
elif age <18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

"""Know that the condition those not always need to end with else block, if it was needed that 
at the end of the of the program a certain condition needs to be checked a program can end with
an ELIF statement."""