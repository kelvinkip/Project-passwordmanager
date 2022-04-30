from os import access
from user import User
from credentials import Credentials
import random

def create_user(fullname,password):
   
    
    new_user = User(fullname,password)
    return new_user

def save_user(user):
   
    user.save_user()
    
def delete_user(user):
       
        user.delete_user()
        
def find_user(username):
   
    return User.find_by_user(username)

def user_exists(username):
    
    return User.user_exists(username)

def create_Credentials(account,username,pass_word):
    
    credentials = Credentials(account,username,pass_word)
    return credentials

def save_credentials(credentials):
    
    credentials.save_credentials()
    
def delete_credential(credentials):

    credentials.delete_credentials()
    
def credential_exist(account):
    
    return Credentials.find_credential_exist(account)

def display_credentials():
    
    return Credentials.display_credentials()

def main():
    print("Welcome to Password manager")
    print("*" * 80)
    print("\n")
    
    while True:
        print("Use these short codes to navigate through: \n 1. New User - NU, \n 2. Login to your account - LG,  \n 3. Display credentials - DC, \n 4. Create Credential - CC \n 5. Generate password - GP \n 6. View Account - VA  \n 7. Exit - EX" )
        print("\n")
        
        short_code = input().upper()
        if short_code == 'NU':
            print("New User")
            print("*" * 80)
            
            print("Enter fullname")
            fullname= input()
            
            print("Enter Password...")
            password = input()
            print("Confirm Password")
            password = input()
            
            save_user(create_user(fullname,password)) #create and save new user account
            
            print('\n')
            print(f"Congratulations!! {fullname} New Account Successfully Created")
            print("*" * 80)
            print('\n')
            print("Proceed to Login!!")
            print("*" * 80)
            print("Enter Short code (LG)")
            print("*" * 80)
            
        elif short_code == 'LG':
            print("Login to your account!!")
            print("*" * 80)
            print("Welcome....")
            print("*" * 80)
            print("Enter Username")
            username = input()
            
            print("Enter Password")
            password = input()
            print(f" Hello {username} Welcome to password Locker!")
            print("*" * 80)
            print("\n")
            
        elif short_code == 'DC':
            
            if display_credentials():
                print("Here are your credentials")
                print("\n")
                
                for Credentials in display_credentials():
                    print(f"{Credentials.account} \n {Credentials.password} \n {Credentials.username}")
                    print("\n")
            else:
                print("\n")
                print("Ooops You don't seem to have any saved Credentials yet ")
                print("*" * 80)
                print("\n")
                print("Create a new Credential")
                print("*" * 80)
                print("\n")
                
        elif short_code == 'CC':
                    print("Account Name \n 1. Twitter \n 2. Facebook \n 3. Instagram")
                    print("*" * 80)
                    print("Enter Account Username")
                    username = input()
                    print("*" * 80)
                    print("Enter Password")
                    password = input()
                    print("*" * 80)
                    print("\n")
                    print("Your Account has been successfully Created")
                    print("*" * 80)
                    print("/n")
                    
        elif short_code == "GP":
            letters = "abcdefghijklmnqryz01234567890ABOPQRSTUVWXYZ!@#$%^&*()?"
            how_many = len(letters)
            print("How long would you like your password to be? ")
            print("*" * 80)
            print(f"p.s: Maximum length of password is {how_many}")
            lent = int(input())
            password = "".join(random.sample(letters, lent))
            print(f"Your password has {lent} characters ")
            print("*" * 80)
            print(password)
            print("*" * 80)
            print("\n")
            
        elif short_code == 'EX':
                print("*" * 80)
                print("Exit Password Locker .........")
                print("*" * 80)
                print("Please Wait")
                print("\n")
                print("*" * 80)
                print("Logged out")
                break
        else:
            print("Invalid Short_code")
            print("Please input the correct short code to continue")
if __name__ == '__main__':
    main()
    