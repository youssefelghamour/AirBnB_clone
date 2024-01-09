#!/usr/bin/python3
'''BaseModel class module'''
import datetime
import uuid


class BaseModel:
    '''defines all common attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        '''initialization'''
        if kwargs != {}:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at':
                    self.created_at = datetime.datetime.fromisoformat(value)
                if key == 'updated_at':
                    self.updated_at = datetime.datetime.fromisoformat(value)
        else:
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


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
