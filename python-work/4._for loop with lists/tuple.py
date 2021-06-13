#a tuple is basically a list that can not be changed through ou the life of a program
dimensions = (200,50)

print(dimensions[0])
print(dimensions[1])
#at point 4 and 5 we print the values of the tuple via indexes one by one

#looping through tuples is also doable
print('\n')

dimensions = (200,50)

for dimension in dimensions:
    print(dimension)

#although its not possible to modify a tuple, you can assign it new values to that tuple's variable

dimensions = (200,50)
print('Original dimensions')
for dimension in dimensions:
    print(dimension)

dimensions = (2400,540)
print('\nModified dimensions')
for dimension in dimensions:
    print(dimension)