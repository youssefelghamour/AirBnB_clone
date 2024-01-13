#!/usr/bin/python3
'''Test module for FileStorage class'''
import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Test class for FileStorage'''
    def setUp(self):
        '''class initializations'''
        self.storage = FileStorage()
        self.new_ins = BaseModel()

    def test_all(self):
        '''Test all method of FileStorage'''
        the_dict = self.storage.all()
        self.assertIsInstance(the_dict, dict)

    def test_new(self):
        '''test new method of FileStorage'''
        self.storage.new(self.new_ins)
        self.assertNotEqual(self.storage.all(), {})
        key = self.new_ins.__class__.__name__ + "." + self.new_ins.id
        self.assertTrue(key in self.storage.all())

    def test_save(self):
        '''test save method of FileStorage'''
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as f:
            content = f.read()
        self.assertTrue(type(content) is str)
        content = json.loads(content)
        self.assertTrue(type(content) is dict)

    def test_all_dict_value_types(self):
        '''test type of values of dictionary returned by all method'''
        self.storage.new(self.new_ins)
        key = self.new_ins.__class__.__name__ + "." + self.new_ins.id
        value = self.storage.all()[key]
        self.assertIsInstance(self.new_ins, type(value))
