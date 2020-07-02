import unittest
from name_func import get_formatted_name

class NameTestCase(unittest.TestCase):
    """" Tests for 'name_func.py' """
    def test_first_last(self):
        formatted_name = get_formatted_name('Jackie','Chan')
        self.assertEqual(formatted_name, 'Jackie Chan')

if __name__ == '__main__':
    unittest.main()