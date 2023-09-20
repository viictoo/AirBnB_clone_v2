#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import os
from models.engine.db_storage import DBStorage


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "test is not suited for database"
)
class TestDBStorage(unittest.TestCase):
    """tests for db storage
    """

    def test_documentation(self):
        """test docs"""
        self.assertIsNotNone(DBStorage.__doc__)
