#now we are going to loop through a slice
players = ['Charles','martina','michael','florence','eli']

print("Here are the first three players on my team:")
for player in players[:3]:
#because of the slice in the for loop python goes through the first three players only
    print(f"\t{player.title()}")