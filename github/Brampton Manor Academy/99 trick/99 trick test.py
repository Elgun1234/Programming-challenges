import unittest

from trick_99 import *


class MyFirstTests(unittest.TestCase):

    def factor_test(self):
        self.assertEqual(factor(), 79)

if __name__ == '__main__':
    unittest.main()
