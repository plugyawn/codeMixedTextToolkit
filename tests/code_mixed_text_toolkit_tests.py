import unittest
from code_mixed_text_toolkit import CodeMixedTextToolkit

class PeTeRTestCase(unittest.TestCase):
  def setUp(self):
    self.cmtt = CodeMixedTextToolkit()

  def test_zero(self):
    """Test 0"""
    result = self.cmtt.demo_function(0)
    self.assertEqual(result, "The number you gave is even.")

  def test_odd_number(self):
    """Test odd number 333"""
    result = self.cmtt.demo_function(333)
    self.assertEqual(result, "The number you gave is odd.")  

  def test_even_number(self):
    """Test even number 420"""
    result = self.cmtt.demo_function(420)
    self.assertEqual(result, "The number you gave is even.")

  def test_negative_number(self):
    """Test negative odd number -42069"""
    result = self.cmtt.demo_function(-85)
    self.assertEqual(result, "The number you gave is odd.")

if __name__ == '__main__':
  unittest.main()