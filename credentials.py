import unittest
from user import User
import pyperclip

class TestUser(unittest.TestCase):
    '''
   

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("kelvin", "kiplangat", "0728335615", "kelvinkipla@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, "kelvin") 
        self.assertEqual(self.new_user.last_name, "kiplangat")
        self.assertEqual(self.new_user.phone_number, "0728335615")
        self.assertEqual(self.new_user.email, "kelvinkipla@gmail.com")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = [] 


    def test_save_contact(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_contact(self):
        self.new_user.save_user()
        test_user = User("Test", "User", "0728335615","test@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test", "User", "0728335615","test@user.com")
        test_user.save_contact() 

        self.new_user.delete_user() 
        self.assertEqual(len(User.user_list), 1) 

    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''
        self.new_user.save_user()
        test_user = User("Test", "User", "0712345678","test@user.com")
        test_user.save_user()

        found_user = User.find_by_user("0728335615") 
        self.assertEqual(found_user.email, test_user.email)

    def test_user_exists(self):
        '''
        
        '''
        self.new_user.save_user() 
        test_user = User("Test", "User", "0728335615","test@user.com") 
        test_user.save_user()

        user_exists = User.user_exists("0728335615") 
        self.assertTrue(user_exists) 

    def test_display_all_user(self):
        '''
        
        '''
        self.assertEqual(User.display_user(), User.user_list) 


    def test_copy_email(self):
    
        self.new_user.save_user() 
        User.copy_email("07283356145") 
        self.assertEqual(self.new_user.email, pyperclip.paste()) 


if __name__ == "__main__":
    unittest.main()   