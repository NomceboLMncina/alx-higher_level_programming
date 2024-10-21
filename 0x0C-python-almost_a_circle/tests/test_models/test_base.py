#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
from models.base import Base
import json
import os


class TestBase(unittest.TestCase):
    """Test the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_auto_increment_id(self):
        """Test automatic ID incrementation."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test assigning a custom ID."""
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_to_json_string_empty(self):
        """Test converting an empty list to a JSON string."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_none(self):
        """Test converting None to a JSON string."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string(self):
        """Test converting a list of dictionaries to JSON string."""
        dicts = [{"id": 1, "width": 10}, {"id": 2, "height": 20}]
        json_str = Base.to_json_string(dicts)
        self.assertEqual(json.loads(json_str), dicts)

    def test_from_json_string_empty(self):
        """Test converting an empty JSON string."""
        json_list = Base.from_json_string("")
        self.assertEqual(json_list, [])

    def test_from_json_string_none(self):
        """Test converting None from JSON string."""
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_string(self):
        """Test converting a JSON string to a list of dictionaries."""
        json_str = '[{"id": 1, "width": 10}, {"id": 2, "height": 20}]'
        dicts = Base.from_json_string(json_str)
        self.assertEqual(dicts, [{"id": 1, "width": 10}, {"id": 2, "height": 20}])

    def test_save_to_file_none(self):
        """Test saving None to a file."""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_empty(self):
        """Test saving an empty list to a file."""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file(self):
        """Test saving a list of Base objects to a file."""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [{"id": 1}, {"id": 2}])

    def test_load_from_file_no_file(self):
        """Test loading from a non-existing file."""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        objects = Base.load_from_file()
        self.assertEqual(objects, [])

    def test_load_from_file(self):
        """Test loading Base objects from a file."""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        objects = Base.load_from_file()
        self.assertEqual(objects[0].id, 1)
        self.assertEqual(objects[1].id, 2)

    def test_save_to_file_csv_none(self):
        """Test saving None to a CSV file."""
        Base.save_to_file_csv(None)
        with open("Base.csv", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_csv_empty(self):
        """Test saving an empty list to a CSV file."""
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_load_from_file_csv_no_file(self):
        """Test loading from a non-existing CSV file."""
        if os.path.exists("Base.csv"):
            os.remove("Base.csv")
        objects = Base.load_from_file_csv()
        self.assertEqual(objects, [])

    def tearDown(self):
        """Clean up any files created during tests."""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Base.csv"):
            os.remove("Base.csv")


if __name__ == "__main__":
    unittest.main()
