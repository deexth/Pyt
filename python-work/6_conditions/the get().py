#n case there is key without a value assigned the get() functions comes in handy
alien_0 = {'color':'green', 'speed':'slow'}

points_value = alien_0.get('points','No value assigned')
print(points_value)