#!/usr/bin/python3
"""unittest module"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == 'db',
    "test is not suited for database")
class test_User(test_basemodel):
    """unittest method"""

    def __init__(self, *args, **kwargs):
        """unittest method """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """unittest method """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """unittest method """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ unittest method"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """unittest method """
        new = self.value()
        self.assertEqual(type(new.password), str)
