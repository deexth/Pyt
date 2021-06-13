#working with a file's content
file = open('pi_digits.txt')

with file as f:
	lines = f.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()


print(pi_string)
print(len(pi_string))


#Large files
print("\nPrinting a pi_million_digits.")
file = open('pi_million_digits.txt')

with file as f:
	lines = f.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(f"{pi_string[:60]}....")
print(len(pi_string))

#Now lts check if a given BD is in the first million digitss of pi

print("\nChecking if a BD is in PI.")
file = 'pi_million_digits.txt'

with open(file) as f:
	lines = f.readlines()
	
birthday =  input("Enter your BD in mmddyy format: ")
if birthday in pi_string:		
	print("\tYour BD  is in the first million PI digits.")
else:
	print("\tYour birthday does not appear in the first million digits of PI.")
