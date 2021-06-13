#using a slice to make a copy of a list
my_foods = ["Pizza",'falafel','carot cake']
friends_foods = my_foods[:]

print("My favorate foods are:")
print(my_foods)
#this first print is the original list
print('\n')

print("My friends favorate foods are:")
print(friends_foods)
#this second print is the copy\


#what does not work is friends_foods = my_foods, as you can see the slice is not there hence it is just the same vaiable not a copy