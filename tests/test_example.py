"""
Unit tests for the example module.
"""

import unittest
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from example import greet, add


class TestExample(unittest.TestCase):
    """Test cases for example functions."""
    
    def test_greet(self):
        """Test the greet function."""
        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice!")
    
    def test_greet_empty_string(self):
        """Test greet with empty string."""
        result = greet("")
        self.assertEqual(result, "Hello, !")
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        result = add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        result = add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_add_mixed_numbers(self):
        """Test adding mixed positive and negative numbers."""
        result = add(5, -3)
        self.assertEqual(result, 2)
    
    def test_add_zero(self):
        """Test adding zero."""
        result = add(0, 5)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
