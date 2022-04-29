from re import S
import unittest
from user import user
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
        self.new_contact = user("kelvin", "kiplangat", "0728335615", "kelvinkipla@gmail.com")

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
        user.contact_list = [] # Empty the contact_list


    def test_save_contact(self):
        self.new_contact.save_contact()
        self.assertEqual(len(user.contact_list), 1)

    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = user("Test", "User", "0728335615","test@user.com")
        test_contact.save_contact()
        self.assertEqual(len(user.contact_list), 2)