#slices
players = ['Charles','martina','michael','florence','eli']

print(players[0:3])
#as for range() function slices also use the same mode of iteration
print('\n')

print(players[1:4])
print('\n')
#for this slice "players[:4]" python will start from the begining and stop at the index in the slice
print(players[:4])
print('\n')
#like for the code above the python starts at the index 2 and stops at the end of the list 
print(players[2:])
print('\n')
#if a ngative number is in a slice it means that python will start from a certain distance from 
#the end of the program depending of the value/s in the slice
print(players[-3:])