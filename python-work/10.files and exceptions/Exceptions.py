#using try-except for the first time

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide a number by zero.")
    
#using try-except to prevent crashes

print("give me two numbers and i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("Enter the first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter the second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
        
#analyzing text
print("\n")
file = 'Alicee.txt'
try:
    with open(file, encoding='utf-8') as ff:
        contents = ff.read()
except FileNotFoundError:
    print("Sorry, the text file 'Alicee' doesn't exist.")
    
print("\n")

file = 'alice.txt'

try:
    with open(file, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry, the text file 'Alicee' doesn't exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {file} has {num_words} words.")

print("\n")

#using the try-except in a function
def count_words(filename):
    """count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename}' has about {num_words} words.")


filenames = ['alice.txt', 'siddhatha.txt', 'moby-dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)

