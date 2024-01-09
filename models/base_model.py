#!/usr/bin/python3
'''BaseModel class module'''
import datetime
import uuid


class BaseModel:
    '''defines all common attributes/methods for other classes'''
    def __init__(self):
        '''initialization'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        '''defines how the should be represented as a string'''
        return ("[{}] ({}) {}".format(__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''updates the attribute updated_at with the current datetime'''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of the instance'''
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        res = self.__dict__
        res['__class__'] = __class__.__name__
        return res
