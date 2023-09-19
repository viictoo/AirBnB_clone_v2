#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from models import *
import unittest
import MySQLdb
from models.engine.db_storage import DBStorage

DB_CONFIG = {
    'host': 'localhost',
    'user': 'hbnb_test',
    'password': 'hbnb_test_pwd',
    'database': 'hbnb_test_db',
}


class TestDBStorage(unittest.TestCase):

    def setUp(self):
        # Set up a connection to the test database
        self.conn = MySQLdb.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()

        # Initialize DBStorage
        self.db_storage = DBStorage()
        self.db_storage.reload()

    def tearDown(self):
        # Clean up after each test
        self.cursor.close()
        self.conn.close()

    def get_state_count(self):
        # Get the number of current records in the 'states' table
        query = "SELECT COUNT(*) FROM states"
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]

        # Close the cursor to release resources
        self.cursor.close()
        # Open a new cursor
        self.cursor = self.conn.cursor()
        return result

    def test_add_state_command(self):
        # Get the initial count of 'states'
        initial_count = self.get_state_count()

        state = State(name="California")
        self.db_storage.new(state)
        self.db_storage.save()
        self.conn.commit()

        # Get the count of 'states' after the command execution
        updated_count = self.get_state_count()
        # print(updated_count)

        # Check if the difference is +1
        self.assertEqual(updated_count - initial_count, 1)

        self.db_storage.delete(state)
        self.conn.commit()

        # Get the count of 'states' after the command execution
        updated_count = self.get_state_count()
        # print(updated_count)

        # Check if the difference is +1
        self.assertEqual(updated_count - initial_count, 0)

    def test_reload_command(self):
        # Get the number of current records in the 'states' table
        query = "DROP DATABASE IF EXISTS hbnb_test_db"
        self.cursor.execute(query)
        query = "CREATE DATABASE IF NOT EXISTS hbnb_test_db"
        self.cursor.execute(query)
        query = "SELECT COUNT(*) \
            FROM information_schema.tables \
                WHERE table_schema = 'hbnb_test_db'"
        self.cursor.execute(query)
        initial_state = self.cursor.fetchone()[0]
        self.conn.commit()

        # reload to create all tables
        self.db_storage.reload()

        query = "SELECT COUNT(*)\
                FROM information_schema.tables\
                WHERE table_schema = 'hbnb_test_db'"
        self.cursor.execute(query)
        final_state = self.cursor.fetchone()[0]

        # Check if al 7 tables were created
        self.assertEqual(final_state - initial_state, 7)


if __name__ == '__main__':
    unittest.main()
