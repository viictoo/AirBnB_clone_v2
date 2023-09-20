#!/usr/bin/python3
"""unittest module """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os


class test_review(test_basemodel):
    """unittest method  """

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        def __init__(self, *args, **kwargs):
            """ unittest method """
            super().__init__(*args, **kwargs)
            self.name = "Review"
            self.value = Review

        def test_place_id(self):
            """ unittest method """
            new = self.value()
            self.assertEqual(type(new.place_id), str)

        def test_user_id(self):
            """unittest method  """
            new = self.value()
            self.assertEqual(type(new.user_id), str)

        def test_text(self):
            """unittest method  """
            new = self.value()
            self.assertEqual(type(new.text), str)
