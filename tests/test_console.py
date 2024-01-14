#!/usr/bin/python3
'''Test module for console'''
import unittest
from console import HBNBCommand
import sys
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    '''Test class for console module'''
    classes = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']

    def test_quit_cmd(self):
        '''test quit command of console'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        res = f.getvalue()
        self.assertEqual("", res)
        self.assertTrue(len(res) == 0)

    def test_EOF(self):
        '''test EOF for console'''
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help(self):
        '''test help for console'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        help_str = '''
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

'''
        self.assertEqual(help_str, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        help_quit = 'Quit command to exit the program\n'
        self.assertEqual(help_quit, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        help_quit = 'EOF exit to the program\n'
        self.assertEqual(help_quit, f.getvalue())

    def test_emptyline(self):
        '''test empty input line for console'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        res = f.getvalue()
        self.assertEqual("", res)

    def test_create(self):
        '''test create command'''
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(class_name))
            class_id = f.getvalue()[:-1]
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all {}".format(class_name))
            self.assertTrue(class_id in f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NotClass")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class doesn't exist **")

    def test_show(self):
        '''test show command'''
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(class_name))
            class_id = f.getvalue()[:-1]
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} {}".format(class_name, class_id))
            res = f.getvalue()[:-1]
            self.assertTrue(class_id in res)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NotClass")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class doesn't exist **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** instance id missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 564sdg654fg6f4g6")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** no instance found **")

    def test_class_show_id(self):
        '''test show advanced show command'''
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(class_name))
            class_id = f.getvalue()[:-1]
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('{}.show("{}")'.format(class_name,
                                                            class_id))
            res = f.getvalue()
            self.assertTrue(class_id in res)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".show()")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class name missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("NotClass.show()")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** class doesn't exist **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** instance id missing **")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show(s5d4g6fg466g4f65g"")')
        error = f.getvalue()[:-1]
        self.assertEqual(error, "** no instance found **")
