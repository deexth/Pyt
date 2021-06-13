#Lets try nesting through a list of dictionary
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color' :'yellow', 'points': 10}
alien_2 = {'color' :'red', 'points': 15}
#we just made 3 dictionaries of aliens, now we put them in a list
aliens = [alien_0, alien_1, alien_2]

#now we are going to loop through the list
for alien in aliens:
    print(alien)

"""Now that we have seen how to loop through a list of dictionaries
 lest try making an empty list and add the dictionaries. """
print("\n")
aliens_1 = []

#lets make atleast 30 aliens
for alien in range(350):
    new_alien = {'color': 'green', 'points': 10, 'speed': 'slow'}
    aliens_1.append(new_alien)

#show the first 5 aliens
for alien in aliens_1[:5]:
    print(alien)
print("...")

#show how many aliens have been created
print(f"Total number of aliens created is: {len(aliens_1)}")

print("\n")
#lets add a twist and make the first thirteen aliens yellow

for alien in aliens_1[:53]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 20

print("Now the aliens are changed")
for alien in aliens_1[:8]:
    print(f"\t{alien}")
print("...")

#lets change some more aliens by adding another condition at the if statement
for alien in aliens_1[23:43]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 20
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 32

print("Now the aliens are changed for a second time")
for alien in aliens_1[:45]:
    print(f"\t{alien}")
print("...")
