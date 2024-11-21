import unittest
from console import *

class TestPalindromeAndMiroir(unittest.TestCase):
    """Tests pour les fonctions est_palindrome et miroir"""

    def test_est_palindrome(self):
        """Test de la fonction est_palindrome"""
        self.assertTrue(est_palindrome("radar"))  # Palindrome simple
        self.assertFalse(est_palindrome("python"))  # Pas un palindrome

    def test_miroir(self):
        """Test de la fonction miroir"""
        self.assertEqual(miroir("hello"), "olleh")

if __name__ == "__main__":
    unittest.main()
