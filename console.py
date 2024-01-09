#!/usr/bin/python3
'''console module'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''simple command interpreter class'''
    prompt = '(hbnb)'

    def do_EOF(self, line):
        '''EOF exit to the program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        '''empty line shouldn’t execute anything'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
