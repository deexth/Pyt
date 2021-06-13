#to print a series of numbers in python the range function is used
for value in range(1,5):
    #though it should be known that in the range function the last number is 
    #not printed only numbers 1 through 4
    print(value)

print('\n')
#you can always convert a set of numbers into a list by adding the list() function arround range()
numbers=list(range(1,6))
print(numbers)