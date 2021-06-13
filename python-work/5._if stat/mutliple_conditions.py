#we will be using AND, OR command
age_0 = 22
age_1 = 18

if (age_0 >= 21) or (age_1 >= 21):
    print("True")
else:
    print("False")

""""For the first 2 conditions we used an OR therefore we only need 1 condition to be true 
in order to have the appropriate message."""

print("\n")

if (age_0 >= 21) and (age_1 >= 21):
    print("True")
else:
    print("False")

"""For the last 2 conditions we used an AND hence all the conditions have to be true in order 
to have the appropriate message"""