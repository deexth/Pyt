#while using capital letters in a list while sorting the compiler considers the values with capital letters first.
cars=["bmw","audi","toyota","subaru"]
#sorting the list
cars.sort()
print(cars)
#once you sort using the sort command there is no going back to the original list.
cars.sort(reverse=True)
print(cars)
#if you want to use a more temporary command for sorting you can use the sorted() function
cars=["bmw","Audi","toyota","Subaru"]
print(sorted(cars))
print(cars)
#using reverse=true in the sorted() function
cars=["bmw","audi","toyota","subaru"]
print(sorted(cars,reverse=True))
print(cars)
#to display a reversed order, but not alphabetically, you can use the reverse() function
cars.reverse()
print(cars)
#to check the length of a list you can use the function len()
print(len(cars))