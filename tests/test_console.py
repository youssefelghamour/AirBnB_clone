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

    def test_EOF(self):
        '''test EOF for console'''
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("EOF")

    def test_help(self):
        '''test help cmd for console'''
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help show")
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help quit")
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help EOF")
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help create")
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help destroy")
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help all")
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help update")

    def test_create(self):
        '''test create <class_name> for console'''
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create User")
