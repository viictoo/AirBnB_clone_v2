#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import console


class TestConsole(unittest.TestCase):
    """tests for db storage
    """

    def test_console_doc(self):
        """unittest for console docstring"""
        self.assertIsNotNone(console.__doc__)


if __name__ == "__main__":
    unittest.main()
