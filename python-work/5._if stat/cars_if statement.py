#the if statement
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
        #at the first condition when car equals to bmw it will be printed in capital letters
    else:
        print(car.title())
        #for this condition all cars remaining will be displayed in title form