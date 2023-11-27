# The first letter of a class name must always be Capital letter
class Example:
    # useful as a placeholder when a statement is required syntactically, but no code needs to be executed (yet)
    pass


# Creating object from a class
example_1 = Example()
# How to create attribute?
# An attribute is a variable that's associated with an object.
example_1.id = "001"
example_1.username = "Angela"


# --------------------------------------------------------------------------------------------------------

# Constructor
class User:
    def __init__(self, user_id, username):
        """
        __INIT FUNCTION__
        Use to initialize the attributes of a class

        You can have as many parameters as you like, the parameter will be passed
        in when an object gets constructed from this class. Once you receive the data,
        you can set the object's attribute.
        """
        self.id = user_id
        self.username = username
        self.followers = 0
        # initialize attribute


# Must always provide the arguments
user_1 = User("001", "Andy")
user_1.followers = 1000
user_2 = User("002", "Qiyang")

print(f"{user_1.username}'s User ID  is: {user_1.id}")
print(f"{user_1.username} got {user_1.followers} followers")
print(f"{user_2.username}'s User ID  is: {user_2.id}")
print(f"{user_2.username} got {user_2.followers} followers\n")
# ---------------------------------------------------------------------------------
# Adding METHODS to a class
class Car:
    def __init__(self):
        self.seats = 5

    # Creating a method to reduce the seats from 5 to 2
    def enter_race_mode(self):
        self.seats = 2


my_car = Car()
print(f"My car have {my_car.seats} seats")
my_car.enter_race_mode()
print(f"My car now have {my_car.seats} seats")
