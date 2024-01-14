#!/usr/bin/python3
'''Test module for console'''
import unittest
from console import HBNBCommand
import sys
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    '''Test class for console module'''
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
