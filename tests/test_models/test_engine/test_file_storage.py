#!/usr/bin/python3
'''Test module for FileStorage class'''
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Test class for FileStorage'''
    def setUp(self):
        '''class initializations'''
        storage = FileStorage()
        new_ins = BaseModel()

    def test_all(self):
        '''Test all method of FileStorage'''
        self.assertEqual(storage.all(), {})
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        '''test new method of FileStorage'''
        storage.new(new_ins)
        self.assertNotEqual(storage.all(), {})
        key = new_ins.__class__.__name__ + "." + new_ins.id
        self.assertTrue(key in storage.all())

    def test_save(self)
