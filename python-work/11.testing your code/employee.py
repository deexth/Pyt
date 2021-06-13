#employee class
class Employee:
    """A class to represent an employee."""
    
    def __init__(self, first, last, salary, middle=''):
        """Initialize the employee."""
        
        self.first = first
        self.last = last
        self.salary = salary
        self.middle = middle
        
    def give_raise(self, amount=5_000):
        """Give the employee a raise"""
        self.salary += amount
        return self.salary
    
    def display_names(self):
        """Display the employee's names"""
        names = f"{self.first}, {self.last}"
        if self.middle:
            names += f" {self.middle}"
        print(names)
        
    def display_salary(self):
        """Display the employee's raise."""
        
        print(self.salary)
