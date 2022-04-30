from os import access
from user import User
from credentials import TestUser
import random

def create_user(fullname,password):
    '''
    function  to create a new user
    '''
    
    new_user = User(fullname,password)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()
    
def delete_user(user):
        '''
        function to delete user
        '''
        user.delete_user()
        
def find_user(username):
    '''
    function that finds user by name and returns the user
    '''
    return User.find_by_user(username)