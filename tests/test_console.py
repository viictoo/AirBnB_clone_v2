#!/usr/bin/python3
"""test module
"""
import io
import sys
import json
import models
import console
import unittest
import pycodestyle
from os import remove
from uuid import UUID
from os.path import isfile
from datetime import datetime
from io import StringIO as SIO
from console import HBNBCommand
from models.base_model import BaseModel
from unittest.mock import create_autospec, patch
import unittest
import os


class TestConsole(unittest.TestCase):
    """unit tests for the console
    """
    def setUp(self):
        """set up test tools
        """
        self.SimIn = HBNBCommand()
        self.out = SIO()

    def tearDown(self):
        """destroy created test elements
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstrings(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(console.__doc__) >= 1)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        def test_emptyline(self):
            """Test no user input"""
            with patch('sys.stdout', SIO()) as SimOut:
                self.SimIn.onecmd("\n")
                self.assertEqual(SimOut.getvalue(), '')

        def test_show_success(self):
            """unittest module"""
            with patch('sys.stdout', SIO()) as SimOut:
                self.SimIn.onecmd('create Place')
                output = SimOut.getvalue().strip()

                instance_id = output

            with patch('sys.stdout', SIO()) as SimOut:
                self.SimIn.onecmd(f'show Place {instance_id}')
                show_output = SimOut.getvalue().strip()

                self.assertTrue(show_output.startswith("[Place"))
                self.assertIn(instance_id, show_output)
                self.assertIn("'created_at': datetime.datetime", show_output)
                self.assertIn("'updated_at': datetime.datetime", show_output)

        def test_show_default_success(self):
            """test show"""
            with patch('sys.stdout', SIO()) as SimOut:
                self.SimIn.onecmd('create Place')
                output = SimOut.getvalue().strip()

                instance_id = output

            with patch('sys.stdout', SIO()) as SimOut:
                self.SimIn.onecmd(f'show Place {instance_id}')
                show_output = SimOut.getvalue().strip()

                self.assertTrue(show_output.startswith("[Place"))
                self.assertIn(instance_id, show_output)
                self.assertIn("'created_at': datetime.datetime", show_output)
                self.assertIn("'updated_at': datetime.datetime", show_output)

        def test_destroy_success(self):
            """test destroy"""
            with patch('sys.stdout', SIO()) as SimOut:
                self.SimIn.onecmd('create Place')
                instance_id = SimOut.getvalue().strip()
                SimOut.truncate(0)
                SimOut.seek(0)
                self.SimIn.onecmd('create Place')
                instance2_id = SimOut.getvalue().strip()
                SimOut.truncate(0)
                SimOut.seek(0)

            with patch('sys.stdout', SIO()) as SimOut:
                self.SimIn.onecmd(f'destroy Place {instance_id}')
                SimOut.truncate(0)
                SimOut.seek(0)
                self.SimIn.onecmd(f'show Place {instance_id}')
                show_output = SimOut.getvalue().strip()
                self.assertEqual("** no instance found **", show_output)
                SimOut.truncate(0)
                SimOut.seek(0)
                self.SimIn.onecmd(f'destroy Place {instance2_id}')
                SimOut.truncate(0)
                SimOut.seek(0)
                self.SimIn.onecmd(f'show Place {instance2_id}')
                show_output2 = SimOut.getvalue().strip()
                self.assertEqual("** no instance found **", show_output2)

            with patch('sys.stdout', SIO()) as SimOut:
                models.storage._FileStorage__objects.clear()
                self.SimIn.onecmd("all Place")
                output = SimOut.getvalue().strip()
                # Confirm output is Empty
                self.assertEqual(output, "[]")
                self.SimIn.onecmd("create Place")
                self.SimIn.onecmd("create Place")
                SimOut.truncate(0)
                SimOut.seek(0)
                self.SimIn.onecmd("all Place")
                output = SimOut.getvalue().strip()
                # Check if the output starts and ends with expected text
                self.assertTrue(output.startswith('["['))
                self.assertTrue(output.endswith('"]'))

            with patch('sys.stdout', SIO()) as SimOut:
                models.storage._FileStorage__objects.clear()
                self.SimIn.onecmd("all User")
                output = SimOut.getvalue().strip()
                # Confirm output is Empty
                self.assertEqual(output, "[]")
                self.SimIn.onecmd("create User")
                self.SimIn.onecmd("create User")
                SimOut.truncate(0)
                SimOut.seek(0)
                self.SimIn.onecmd("all User")
                output = SimOut.getvalue().strip()
                # Check if the output starts and ends with expected text
                self.assertTrue(output.startswith('["['))
                self.assertTrue(output.endswith('"]'))


if __name__ == "__main__":
    unittest.main()
