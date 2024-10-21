#!/usr/bin/python3
"""
Test for the Square class
"""

import unittest
import pep8
import inspect
import io
from contextlib import redirect_stdout
from models import square
from models.base import Base
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """Tests the Square class' style and documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.sq_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8_conformance_square(self):
        """Test that models/square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_square(self):
        """Test that tests/test_models/test_square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.sq_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestSquare(unittest.TestCase):
    """Test the functionality of the Square class"""
    @classmethod
    def setUpClass(cls):
        """Set up the tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)

    def test_size(self):
        """Test for functioning size"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_width(self):
        """Test width"""
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s3.width, 4)
        self.assertEqual(self.s4.width, 7)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 4)
        self.assertEqual(self.s4.height, 7)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_mandatory_size(self):
        """Test that size is a mandatory arg"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_size_typeerror(self):
        """Test non-ints for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_x_typeerror(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, True)

    def test_y_typeerror(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, True)

    def test_size_valueerror(self):
        """Test ints <= 0 for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_area(self):
        """Test area"""
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 49)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            a = self.s1.area(1)

    def test_basic_display(self):
        """Test display without x and y"""
        s = Square(3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s1.display()
            output = buf.getvalue()
            self.assertEqual(output, "#\n")
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.s1.display(1)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (2) 3/0 - 2")
        self.assertEqual(str(self.s3), "[Square] (3) 5/6 - 4")
        self.assertEqual(str(self.s4), "[Square] (10) 8/9 - 7")

    def test_display_xy(self):
        """Testing the display method with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 3 + "#" * 2 + "\n") * 2)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.s3.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 6 +
                             (" " * 5 + "#" * 4 + "\n") * 4)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.s4.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 9 +
                             (" " * 8 + "#" * 7 + "\n") * 7)

    def test_update_args(self):
        """Testing the update method with *args"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 2")
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/0 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_update_kwargs(self):
        """Testing the update method with **kwargs"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(id=89)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s.update(size=2)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 2")
        s.update(x=3, y=4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")
        s.update(size=5, x=1, y=2)
        self.assertEqual(str(s), "[Square] (89) 1/2 - 5")

    def test_to_dictionary(self):
        """Testing the to_dictionary method"""
        s = Square(1, 2, 3, 4)
        expected_dict = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_no_args(self):
        """Test to_dictionary with no args"""
        with self.assertRaises(TypeError):
            self.s1.to_dictionary(1)

    @classmethod
    def tearDownClass(cls):
        """Tear down the tests"""
        del cls.s1
        del cls.s2
        del cls.s3
        del cls.s4


if __name__ == '__main__':
    unittest.main()
