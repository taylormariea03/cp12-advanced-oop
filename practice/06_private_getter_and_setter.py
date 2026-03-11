from helper_functions import clear_screen
clear_screen()

# ===================
# GETTERS AND SETTERS
# ===================

'''
OVERVIEW
--------
Whenever you have a private variable, the way to give access to the variable
outside of the class (or in an inherited class) is to create a method that
just returns that private variable (called a getter) and a method that sets
a new value for a private variable (called a setter).
'''

class User:
    def __init__(self, user_id: str):
        self.__id = None #id is a private variable
        self.set_id(user_id)
    
    def get_id(self):
        return self.__id
    
    def set_id(self, user_id):
        if not isinstance(user_id, str) or len(user_id) != 8:
            raise ValueError('ID does not meet requirements')
        self.__id = user_id
    
user_obj = User("12345678")

print(user_obj.get_id())

# 1. ADDING A GETTER AND A SETTER
# Make the id instance variable private. Then create a method called "get_id"
# that will return the id. Then also create a method called "set_id" that will
# set a new id as long as it is a string that is exactly 8 characters long.



'''
TIP:
----

When doing some kind of data validation, like in the above example, if the 
requirements for the variable aren't met (like it must be example 8 characters
long, etc.) you can raise an error, like this:

if len(my_input): != 8
    raise ValueError("The user id must be exactly 8 characters long")

'''