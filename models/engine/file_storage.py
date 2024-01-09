#!/usr/bin/python3
""" FileStorage class Module """
from models.base_model import BaseModel
import json


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file
        to instances

        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - stores all objects by <class name>.id
                                (ex: with id=12121212, the key will be
                                    BaseModel.12121212)"""

    __file_path = __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
            creates a new object (element) in the objects dictionary

            key = <obj class name>.id
            Value = dictionary representation of obj (obj.to_dict())
            """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        json_objs = {}
        for key in self.__objects:
            json_objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_objs, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as file:
                json_objs = json.load(file)
            for key in json_objs:
                self.__objects[key] = BaseModel(**json_objs[key])
        except:
            pass
