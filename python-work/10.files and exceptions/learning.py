#Using the replace() function
file = 'learning.txt'

with open(file) as f:
	line = f.readlines()

for msg in line:
	msg = msg.strip()
	print(msg)

print("\nNow changing C to Pyhton:")
for msg in line:	
	print(f"\t{msg.replace('C', 'Python')}")

