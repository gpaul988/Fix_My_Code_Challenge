#!/usr/bin/python3
""" 
Graham S. Paul (user.py) - User class
"""


class User():
    """ Details """

    def __init__(self):
        """ Details """
        self.__email = None


    @property
    def email(self):
        """ Details """
        return self.__email


    @email.setter
    def email(self, value):
        """ Details """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
    

if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)