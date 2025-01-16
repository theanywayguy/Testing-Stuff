import unittest
from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """CHECK THAT 1 ISNT A PRIME."""
        self.assertFalse(is_prime(1))
    
    def test_2(self):
        """CHECK THAT 2 IS A PRIME."""
        self.assertTrue(is_prime(2))
    def test_8(self):
        """CHECK THAT 8 ISNT A PRIME."""
        self.assertFalse(is_prime(8))
    def test_11(self):
        """CHECK THAT 11 IS A PRIME."""
        self.assertTrue(is_prime(11))


if __name__== "__main__":
    unittest.main()