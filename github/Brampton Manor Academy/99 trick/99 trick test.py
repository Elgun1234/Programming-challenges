import unittest

from trick_99 import *


class MyFirstTests(unittest.TestCase):

    def test_factor_equals(self):
        self.assertEqual((15), friend(99-15))

if __name__ == '__main__':
    unittest.main()
