#!/usr/bin/python3
"""test module """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == 'db',
    "test is not suited for database")
class test_Amenity(test_basemodel):
    """test amenity class"""

    def __init__(self, *args, **kwargs):
        """init tests"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """test no 2"""
        new = self.value()
        self.assertEqual(type(new.name), str)
