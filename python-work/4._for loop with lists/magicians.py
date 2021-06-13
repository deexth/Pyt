magicians=['alice','david','carolina']
#declaring a list of magicians
for magician in magicians:
    #printing the list of magicians simply
    print(magician)

#using the same loop but print a message with the names of the magicians
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    #adding more messages after the display 
    print(f"I can't wait to see your next trick, {magician.title()}")
    #If {} are not arround the variable "magician.title()"
    #the display will be a simple message no magicians will be displayed

#after an identation a new message can be added that will not be part of the loop
print("Thank you, everyone. That was a great magic show.")
