#!/usr/bin/python3
""" Unittest for the BaseModel class in the base_model module """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Tests the BaseModel class """

    def test_init_id(self):
        """ Tests with a custom id """
        model = BaseModel(id=5)
        self.assertEqual(model.id, 5)

    def test_init_id_negative(self):
        """ Tests with a custom negative id """
        model = BaseModel(id=-4)
        self.assertEqual(model.id, -4)

    def test_init_id_float(self):
        """ Tests with a custom float id """
        model = BaseModel(id=654.3)
        self.assertEqual(model.id, 654.3)

    def test_init_name(self):
        """ Tests with a custom instance attribute """
        model = BaseModel(name="first_model")
        self.assertEqual(model.name, "first_model")

    def test_str(self):
        """ Tests the string representation of the model with
            custom instances attributes """
        model = BaseModel(id=2, name="model1")
        s = "[BaseModel] (2) {'id': 2, 'name': 'model1'}"
        self.assertEqual(str(model), s)

    def test_str2(self):
        """ Tests the string representation of the model """
        model = BaseModel()
        s = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), s)

    def test_to_dict(self):
        """ Tests the dictionary representation of the model """
        model = BaseModel()
        self.assertEqual(model.to_dict(), model.__dict__)

    def test_to_dict2(self):
        """ Tests the dictionary representation of the model
            with custom attributes """
        date = datetime(2024, 1, 10, 17, 48)
        date_str = str(date)
        model = BaseModel(number=15, name="test_model",
                          created_at=date_str, updated_at=date_str)
        self.assertEqual(model.to_dict(), model.__dict__)
