#!/usr/bin/python3
'''console module'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''simple command interpreter class'''
    prompt = '(hbnb)'
    my_dict = {}

    def do_EOF(self, line):
        '''EOF exit to the program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        '''empty line shouldn’t execute anything'''
        pass

    def do_create(self, line):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)'''
        if line == '':
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            ins = BaseModel()
            self.my_dict[ins.id] = ins
            ins.save()
            print(ins.id)

    def do_show(self, line):
        '''Prints the string of an instance based on the class name and id'''
        lst = line.split()
        if len(lst) < 2:
            if len(lst) == 0:
                print("** class name missing **")
            elif lst[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(lst) == 1 and lst[0] == 'BaseModel':
                print("** instance id missing **")
        elif len(lst) == 2:
            if lst[1] not in self.my_dict:
                print("** no instance found **")
            else:
                for key, value in self.my_dict.items():
                    if key == lst[1]:
                        the_dict = value.__dict__
                        base_ins = BaseModel(**the_dict)
                        print(base_ins)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
