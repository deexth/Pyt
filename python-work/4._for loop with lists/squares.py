#list of squares
squares = []
#Fisrt we start by creating an empty list
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)
#after looping through the loop at step 6 we append the values of the squares

#or to reduce the lines the line number 5 can be put in line number 6
print("\n")

squares = []

for value in range(1,11):
    squares.append(value ** 2)

print(squares)
#instead of using an additional variable like in the top program 
#sqaure was deleted and (value ** 2) was put int the append() function
#Not only the above functions can be used but also min(), max() and sum() functions.