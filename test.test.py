import unittest
from calculator import stringcalculator 
class TestStringcal(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(0,stringcalculator(""))

    def test_simple_output(self):
        self.assertEqual(6,stringcalculator("1,2,3"))

    def test_newlineandcomma_String(self):
        self.assertEqual(10,stringcalculator("1\n2,3\n4"))

    def test_customdelimeters_string(self):
        self.assertEqual(stringcalculator("//[:::][.][**]\n1:::2.3**4"),10)

if __name__ == "__main__":
    unittest.main()

