import unittest

from rod_conversion import *


class MyFirstTests(unittest.TestCase):

    def test_metres(self):
        self.assertEqual(metres(1), 0.19883878151594686)

  

if __name__ == '__main__':
    unittest.main()
