import unittest
import utils

class TestIsPalindromeMethod(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(utils.is_palindrome('racecar'))

    def test_non_palindrome(self):
        self.assertFalse(utils.is_palindrome('ball state'))

    def test_palindrome_with_special_characters(self):
        self.assertTrue(utils.is_palindrome('A man, a plan, a canal - Panama!'))

    def test_non_string_failure(self):
        self.assertRaises(TypeError, utils.is_palindrome, 1)

if __name__ == '__main__':
    unittest.main()
