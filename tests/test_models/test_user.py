#!/usr/bin/python3
'''Test module for User class'''
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''unittest of the User class'''
    def test_attr(self):
        '''test attributes of User class'''
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def test_User_instance(self):
        '''test User class with an instance'''
        ins = User()
        self.assertIsInstance(ins, User)
        self.assertTrue(issubclass(type(ins), BaseModel))
