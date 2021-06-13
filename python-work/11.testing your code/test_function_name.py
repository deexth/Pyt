import unittest
from return_values import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for 'return_values.py'"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('Janis', 'Jonas')
        self.assertEqual(formatted_name, 'Janis Jonas')
        
    def test_first_last_middle_name(self):
        """Do names with middles"""
        formatted_name = get_formatted_name('Janis', 'Jonas', 'jonah')
        self.assertEqual(formatted_name, 'Janis Jonas Jonah')


if __name__ == '__main__':
    unittest.main()
