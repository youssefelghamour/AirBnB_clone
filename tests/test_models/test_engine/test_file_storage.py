#!/usr/bin/python3
'''Test module for FileStorage class'''
import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        user = User()
        city = City()
        amen = Amenity()
        rev = Review()
        pl = Place()
        state = State()
        self.storage.new(self.new_ins)
        self.storage.new(user)
        self.storage.new(city)
        self.storage.new(amen)
        self.storage.new(rev)
        self.storage.new(pl)
        self.storage.new(state)
        self.assertNotEqual(self.storage.all(), {})
        key = self.new_ins.__class__.__name__ + "." + self.new_ins.id
        self.assertTrue(key in self.storage.all())
        self.assertTrue(self.new_ins in self.storage.all().values())
        self.assertTrue("User" + "." + user.id in self.storage.all())
        self.assertTrue(user in self.storage.all().values())
        self.assertTrue("City" + "." + city.id in self.storage.all())
        self.assertTrue(city in self.storage.all().values())
        self.assertTrue("Amenity" + "." + amen.id in self.storage.all())
        self.assertTrue(amen in self.storage.all().values())
        self.assertTrue("Review" + "." + rev.id in self.storage.all())
        self.assertTrue(rev in self.storage.all().values())
        self.assertTrue("Place" + "." + pl.id in self.storage.all())
        self.assertTrue(pl in self.storage.all().values())
        self.assertTrue("State" + "." + state.id in self.storage.all())
        self.assertTrue(state in self.storage.all().values())

    def test_save(self):
        '''test save method of FileStorage'''
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as f:
            content = f.read()
        self.assertTrue(type(content) is str)
        content = json.loads(content)
        self.assertTrue(type(content) is dict)

    def test_save_with_all_classes(self):
        '''test save method with different classes'''
        user = User()
        city = City()
        amen = Amenity()
        rev = Review()
        pl = Place()
        state = State()
        self.storage.new(self.new_ins)
        self.storage.new(user)
        self.storage.new(city)
        self.storage.new(amen)
        self.storage.new(rev)
        self.storage.new(pl)
        self.storage.new(state)
        self.storage.save()
        with open("file.json", 'r') as f:
            content = f.read()
        self.assertTrue("BaseModel" + "." + self.new_ins.id in content)
        self.assertTrue("User" + "." + user.id in content)
        self.assertTrue("City" + "." + city.id in content)
        self.assertTrue("Amenity" + "." + amen.id in content)
        self.assertTrue("Review" + "." + rev.id in content)
        self.assertTrue("Place" + "." + pl.id in content)
        self.assertTrue("State" + "." + state.id in content)

    def test_all_dict_value_types(self):
        '''test type of values of dictionary returned by all method'''
        self.storage.new(self.new_ins)
        key = self.new_ins.__class__.__name__ + "." + self.new_ins.id
        value = self.storage.all()[key]
        self.assertIsInstance(self.new_ins, type(value))

    def type_of_FileStorage(self):
        '''test the type of FileStorage class'''
        self.assertEqual(type(self.Storage), FileStorage)

    def test_reload(self):
        '''test reload method of FileStorage class'''
        user = User()
        city = City()
        amen = Amenity()
        rev = Review()
        pl = Place()
        state = State()
        self.storage.new(self.new_ins)
        self.storage.new(user)
        self.storage.new(city)
        self.storage.new(amen)
        self.storage.new(rev)
        self.storage.new(pl)
        self.storage.new(state)
        self.storage.save()
        self.storage.reload()
        obj_dict = self.storage.all()
        self.assertTrue("BaseModel" + "." + self.new_ins.id in obj_dict)
        self.assertTrue("User" + "." + user.id in obj_dict)
        self.assertTrue("City" + "." + city.id in obj_dict)
        self.assertTrue("Amenity" + "." + amen.id in obj_dict)
        self.assertTrue("Review" + "." + rev.id in obj_dict)
        self.assertTrue("Place" + "." + pl.id in obj_dict)
        self.assertTrue("State" + "." + state.id in obj_dict)

    def test_save_str_arg(self):
        '''test save method with string argument'''
        with self.assertRaises(TypeError):
            self.storage.save("string")
