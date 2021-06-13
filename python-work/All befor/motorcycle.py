motorcycle=['ducati','honda','suzuki']
motorcycle[0]='yamaha'
print(motorcycle)
#now appending, you can also make an empty list and aappend all the information.
motorcycle.append('ducati')
print(motorcycle) 
#insert helps placing the appended value at the desidered position.
motorcycle.insert(2,'toyota')
print(motorcycle)
#deleting usee the code del
del motorcycle[1]
print(motorcycle)
#popping we use the pop code. you can also use indexes in the paranthesis to pop any string
last_owned=motorcycle.pop(3)
print(f'My last motorcycle wa a {last_owned}.')
#to delete values using the values themselves you can use remove. That is when you do not know the index value of that value
motorcycle.remove("toyota")
print(motorcycle)