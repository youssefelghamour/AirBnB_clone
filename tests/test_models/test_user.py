#!/usr/bin/python3
'''Test module for User class'''
import unittest
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


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

    def test_attr_comp(self):
        '''test User class attributes'''
        attr = {"email": str, "password": str,
                "first_name": str, "last_name": str}
        ins = User()
        for key, value in attr.items():
            self.assertTrue(hasattr(ins, key))
            self.assertEqual(type(getattr(ins, key, None)), value)
