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
def user_exists(username):
    '''
    function that checks if user exists and returns a boolean
    '''
    return User.user_exists(username)

#credentials 
def create_credentials(account,username,pass_word):
    '''
    function to create new credentials
    '''
    credentials = User(account,username,pass_word)
    return credentials

def save_credentials(credentials):
    '''
    function to save a credential
    '''
    credentials.save_credentials()
    
def delete_credential(credentials):
    '''
    function to delete credential
    '''
    credentials.delete_credentials()
    
def credential_exist(account):
    '''
    function that checks if  a credential exists by account and returns a boolean
    '''
    return User.find_credential_exist(account)
