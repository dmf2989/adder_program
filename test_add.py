# test_add.py

import unittest 
from add import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 7), 12)
        
if __name__ == '__main__':
    unittest.main()