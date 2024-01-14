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
        self.assertTrue(HBNBCommand().onecmd("quit"))

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
