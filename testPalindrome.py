import unittest
from code.palindrome import ispalindrome

class testIsPalindrome(unittest.TestCase):

	def testicle1(self):
		self.assertTrue(ispalindrome("racecar"))

	def testicle2(self):
		self.assertFalse(ispalindrome("hello"))

if __name__ == "__main__":
	unittest.main()
