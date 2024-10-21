#!/usr/bin/python3
"""
Test for the Rectangle class
"""

import unittest
import pep8
import inspect
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleDocs(unittest.TestCase):
    """Tests the Rectangle class' style and documentation"""
    
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_conformance_rectangle(self):
        """Test that models/rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """Test the functionality of the Rectangle class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up for the tests"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(11, 12, 13, 14)

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 9)
        self.assertEqual(self.r4.id, 3)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r4.width, 11)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r3.height, 6)
        self.assertEqual(self.r4.height, 12)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 7)
        self.assertEqual(self.r4.x, 13)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 8)
        self.assertEqual(self.r4.y, 14)

    def test_mandatory_width(self):
        """Test that width is a mandatory arg"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_mandatory_height(self):
        """Test that height is a mandatory arg"""
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_width_typeerror(self):
        """Test non-ints for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)

    def test_height_typeerror(self):
        """Test non-ints for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, True)

    def test_x_typeerror(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, True)

    def test_y_typeerror(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, True)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test ints < 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """Test area"""
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r2.area(), 6)
        self.assertEqual(self.r3.area(), 30)
        self.assertEqual(self.r4.area(), 132)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            r = self.r1.area(1)

    def test_basic_display(self):
        """Test display without x and y"""
        r = Rectangle(2, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 10 + "\n") * 10)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 3)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/6")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 13/14 - 11/12")

    def test_display_xy(self):
        """Testing the display method with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 4 + "#" * 2 + "\n") * 3)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r3.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 8 +
                             (" " * 7 + "#" * 5 + "\n") * 6)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r4.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 14 +
                             (" " * 13 + "#" * 11 + "\n") * 12)

    def test_update_args(self):
        """Testing the update method with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (2) 5/6 - 3/4")

    def test_update_kwargs(self):
        """Testing the update method with **kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(width=4, height=5, x=6, y=7, id=2)
        self.assertEqual(str(r), "[Rectangle] (2) 6/7 - 4/5")

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        expected_dict = {'id': 1, 'width': 10, 'height': 10, 'x': 0, 'y': 0}
        self.assertEqual(self.r1.to_dictionary(), expected_dict)

        expected_dict = {'id': 2, 'width': 2, 'height': 3, 'x': 4, 'y': 0}
        self.assertEqual(self.r2.to_dictionary(), expected_dict)

    def test_to_dictionary_with_args(self):
        """Test that to_dictionary() does not accept args"""
        with self.assertRaises(TypeError):
            self.r1.to_dictionary(1)

    def test_update_with_invalid_args(self):
        """Test update with invalid args"""
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaises(TypeError):
            r.update("hello", 3, 4)

    def test_update_with_too_few_args(self):
        """Test update with too few args"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 1/1")  # only id updated

    def test_update_with_invalid_kwargs(self):
        """Test update with invalid kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaises(TypeError):
            r.update(nonexistent_arg=5)

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests"""
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4


if __name__ == '__main__':
    unittest.main()
