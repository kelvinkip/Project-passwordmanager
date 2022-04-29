from re import S
import unittest
from user import User
import pyperclip

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = User("kelvin", "kiplangat", "0728335615", "kelvinkipla@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_contact.first_name, "kelvin") 
        self.assertEqual(self.new_contact.last_name, "kiplangat")
        self.assertEqual(self.new_contact.phone_number, "0728335615")
        self.assertEqual(self.new_contact.email, "kelvinkipla@gmail.com")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.contact_list = [] 


    def test_save_contact(self):
        self.new_contact.save_contact()
        self.assertEqual(len(User.contact_list), 1)

    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = User("Test", "User", "0728335615","test@user.com")
        test_contact.save_contact()
        self.assertEqual(len(User.contact_list), 2)
    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_contact.save_contact()
        test_contact = User("Test", "User", "0728335615","test@user.com")
        test_contact.save_contact() 

        self.new_contact.delete_contact() 
        self.assertEqual(len(User.contact_list), 1) 

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''
        self.new_contact.save_contact()
        test_contact = User("Test", "User", "0712345678","test@user.com")
        test_contact.save_contact()

        found_contact = User.find_by_number("0728335615") 
        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''
        self.new_contact.save_contact() 
        test_contact = User("Test", "User", "0728335615","test@user.com") 
        test_contact.save_contact()

        contact_exists = User.contact_exists("0728335615") 
        self.assertTrue(contact_exists) 

    def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts saved
        '''
        self.assertEqual(User.display_contacts(), User.contact_list) 


    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''
        self.new_contact.save_contact() 
        User.copy_email("0711432765") 
        self.assertEqual(self.new_contact.email, pyperclip.paste()) 


if __name__ == "__main__":
    unittest.main()   