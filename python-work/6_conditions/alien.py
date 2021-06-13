#dictionaries are consisted of "key-value pairs"
alien_0 = {'color':'green', 'points':5}
#in the above declaraation color and points are keys then green and 5 are there values respectively
print(alien_0['color'])
print(alien_0['points'])
#you can always add new key-value pairs
print("\n")

alien_0['x_position'] = 0
alien_0['y_position'] = 1

print(alien_0)
"""you can always start with an empty dictionary and assing key-value pairs later in the program
 i.e: alien_0 = {}"""

#you can also change the values of the key like may be changing the color of the alien


alien_0['color'] = 'yellow'

print(f"The alien is now {alien_0['color']}.")
#now we are going to delete one key along with its value
print("\n")
del alien_0['points']

print(alien_0)