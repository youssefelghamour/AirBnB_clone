#!/usr/bin/python3
'''Test module for FileStorage class'''
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Test class for FileStorage'''
    def test_all(self):
        '''Test all method of FileStorage'''
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)
