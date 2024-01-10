#!/usr/bin/python3
'''console module'''
import cmd
from models.base_model import BaseModel


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
            ins.save()
            print(ins.id)
            self.my_dict[ins.id] = ins

    def do_show(self, line):
        '''Prints the string of an instance based on the class name and id'''
        x = line.split()
        if len(x) < 2:
            if len(x) == 0:
                print("** class name missing **")
            elif x[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(x) == 1 and x[0] == 'BaseModel':
                print("** instance id missing **")
        elif len(x) == 2:
            if x[1] not in self.my_dict:
                print("** no instance found **")
            for key, value in self.my_dict.items():
                if key == x[1]:
                    print(value)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
