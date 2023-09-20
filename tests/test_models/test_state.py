#!/usr/bin/python3
""" unittest module """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os


class test_state(test_basemodel):
    """unittest class  """

    def __init__(self, *args, **kwargs):
        """unittest method  """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ unittest method """
        new = self.value()
        self.assertEqual(type(new.name), str)
