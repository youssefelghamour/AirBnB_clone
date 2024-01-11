#!/usr/bin/python3
'''console module'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''simple command interpreter class'''
    prompt = '(hbnb) '

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
        elif line not in storage.classes:
            print("** class doesn't exist **")
        else:
            the_class = storage.classes[line]
            ins = the_class()
            ins.save()
            print(ins.id)

    def do_show(self, line):
        '''Prints the string of an instance based on the class name and id'''
        args = line.split()
        if len(args) < 2:
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif args[0] in storage.classes:
                print("** instance id missing **")
        elif len(args) == 2:
            key = "{}.{}".format(args[0], args[1])
            obj_dict = storage.all()
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif key not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[key])

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        args = line.split()
        if len(args) < 2:
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif args[0] in storage.classes:
                print("** instance id missing **")
        elif len(args) == 2:
            key = "{}.{}".format(args[0], args[1])
            obj_dict = storage.all()
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif key not in obj_dict:
                print("** no instance found **")
            else:
                del (storage.all()[key])
                storage.save()

    def do_all(self, line):
        '''Prints all string representation of all instances'''
        the_list = []
        objs_dict = storage.all()
        if line:
            if line not in storage.classes:
                print("** class doesn't exist **")
            else:
                for key, value in objs_dict.items():
                    class_name, x = key.split('.')
                    if class_name == line:
                        the_list.append(str(value))
                print(the_list)
        else:
            for key, value in objs_dict.items():
                the_list.append(str(value))
            print(the_list)

    def do_update(self, line):
        '''Updates an instance by adding or updating attribute'''
        args = line.split()
        obj_dict = storage.all()
        if len(args) < 2:
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif args[0] in storage.classes:
                print("** instance id missing **")
        elif len(args) == 2:
            key = "{}.{}".format(args[0], args[1])
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif key not in obj_dict:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            key = "{}.{}".format(args[0], args[1])
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif key not in obj_dict:
                print("** no instance found **")
            else:
                print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            elif key not in obj_dict:
                print("** no instance found **")
            else:
                for k, v in storage.all().items():
                    if k == key:
                        args[3] = args[3].strip('"')
                        if args[2] in v.__dict__:
                            attr_type = type(getattr(v, args[2]))
                            args[3] = attr_type(args[3])
                        setattr(v, args[2], args[3])
                        v.save()

    def default(self, line):
        ''' Executes the appropiate command (ex: <class name>.command()) '''
        parts = line.split('.')
        class_name = parts[0]
        if len(parts) == 2:
            if parts[1] == 'count()':
                count = 0
                for k, v in storage.all().items():
                    name, x = k.split('.')
                    if class_name == name:
                        count += 1
                print(count)
            elif parts[1] == 'all()':
                self.do_all(class_name)
            elif (parts[1].split('(')[0]) == 'show':
                st = parts[1]
                st = st.split('(')
                command = st[0]
                id_number = st[1]
                id_number = id_number.strip(')').strip('"')
                new_line = "{} {}".format(class_name, id_number)
                self.do_show(new_line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
