#!/usr/bin/python3
"""test module """
from tests.test_models.test_base_model import test_basemodel
from models.city import City

import os


class test_City(test_basemodel):
    """test city class"""

    def __init__(self, *args, **kwargs):
        """unittest method """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """unittest method  """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ unittest method """
        new = self.value()
        self.assertEqual(type(new.name), str)
