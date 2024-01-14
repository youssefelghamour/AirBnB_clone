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
