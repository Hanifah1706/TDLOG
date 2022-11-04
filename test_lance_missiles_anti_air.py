import unittest
from Lance_missiles_anti_air import *
from Exception import *

arm=Lance_missiles_anti_air()
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertRaises(OutOfRangeError, arm.fire_at(0,5,-7))  # add assertion here


if __name__ == '__main__':
    unittest.main()
