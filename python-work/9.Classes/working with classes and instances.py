#car.py,
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make.title()
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())

print("\n Setting a default value for an attribute:")

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make.title()
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #when an instance is created there is no need to pass attributes in parameters
        #as long as these attributes are declared in the __init__ function.


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\t{self.year} {self.make} {self.model}"
        return long_name

           
    def read_odometer(self):
        """
        Print a statement showing the car's mileage.
        """
        print(f"\tThis car has {self.odometer_reading} miles on it.")

my_new_car = Car('BMW', 'X5M',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#modifying attribute values
#lets change the value of odometer_reading
print("\nChanging the odometer reading:")

my_new_car = Car('Audi', 'q8', 2021)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 14
my_new_car.read_odometer()

#modifying attributes value through a method
print("\nModifying attributes value through a method:")

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make.title()
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #when an instance is created there is no need to pass attributes in parameters
        #as long as these attributes are declared in the __init__ function.


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"\t{self.year} {self.make} {self.model}"
        return long_name

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back
        """
        #lets add a twist to the odometer update
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            
        else:
            print("You can't roll back the odometer reading.")


    def read_odometer(self):
        """
        Print a statement showing the car's mileage.
        """
        print(f"\tThis car has {self.odometer_reading} miles on it.")

my_new_car = Car('BMW', 'X6M',2021)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(-23)
my_new_car.read_odometer()
