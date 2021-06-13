#Now lets try to open pi_digits.txt
file = 'pi_digits.txt'
with open(file) as file_object:
    contents = file_object.read()

print(contents.rstrip())

#working line by line
print("Working line by line:")
with open(file) as file_object:
    for line in file_object:
    	print(f"\t- {line.rstrip()}")


#making a list of lines from a file
print("\nAccessing the files contents outside the 'with':")
with open(file) as f:
	lines = f.readlines()

for line in lines:
 	print(line.rstrip())
  
#reading programming.txt
file = 'programming.txt'

with open(file) as p:
    contents = p.read()
    
print(contents)