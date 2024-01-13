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
        ins = User
        self.assertTrue(hasattr(ins, "email"))
        self.assertEqual(type(ins.email), str)
        self.assertTrue(hasattr(ins, "password"))
        self.assertTrue(hasattr(ins, "first_name"))
        self.assertTrue(hasattr(ins, "last_name"))

    def test_User_instance(self):
        '''test User class with an instance'''
        ins = User()
        self.assertIsInstance(ins, User)
        self.assertTrue(issubclass(type(ins), BaseModel))
