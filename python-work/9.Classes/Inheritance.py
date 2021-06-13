#Inheritance basically consists of Parents class and child class which are the one that inherit from the
#parent class
print("User class will be the parent class and admin will be the chhild class")
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")


class Admin(User):
    """Representing the admin class profile"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []


    def show_privileges(self):
        """
        List of admin privileges
        """
        print("These are some of the admin privileges: ")

        for privilege in self.privileges:
            print(f"\t -{privilege.title()}")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = Admin('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()
willie.privileges = ["can add post", "can delete post", "can ban user"]
willie.show_privileges()