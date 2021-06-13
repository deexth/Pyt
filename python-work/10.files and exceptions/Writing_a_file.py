#writing an empty file

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    
#appending new lines to the file

with open(filename, 'a') as file_object:
    file_object.write("I love creating new games.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser,")

with open(filename) as file_object:    
    contents = file_object.read()
    
print(contents)

