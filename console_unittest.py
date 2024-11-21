import unittest
from console import *
from datetime import datetime
from unittest.mock import patch

class TestPalindromeAndMiroir(unittest.TestCase):
    """Tests pour les fonctions est_palindrome et miroir"""

    def test_est_palindrome(self):
        """Test de la fonction est_palindrome"""
        self.assertTrue(est_palindrome("radar"))  # Palindrome simple
        self.assertTrue(est_palindrome("A man a plan a canal Panama"))  # Palindrome avec espaces et majuscules
        self.assertFalse(est_palindrome("python"))  # Pas un palindrome
        self.assertTrue(est_palindrome(""))  # Chaîne vide, considéré comme un palindrome

    def test_miroir(self):
        """Test de la fonction miroir"""
        self.assertEqual(miroir("hello"), "olleh")
        self.assertEqual(miroir("radar"), "radar")  # Palindrome retourne lui-même
        self.assertEqual(miroir(" "), " ")  # Espace unique
        self.assertEqual(miroir("12345"), "54321")  # Nombres







# class TestAuRevoir(unittest.TestCase):
#     """Tests pour la fonction au_revoir"""

#     @patch("console.datetime")
#     def test_au_revoir_day(self, mock_datetime):
#         """Test de au_revoir pendant la journée"""
#         mock_datetime.datetime.now.return_value = datetime(2024, 1, 1, 12, 0, 0)  # Midi
#         with patch("builtins.print") as mock_print:
#             au_revoir()
#             mock_print.assert_called_with("Au revoir!")  # Vérifie le message "Au revoir!"

#     @patch("console.datetime")
#     def test_au_revoir_night(self, mock_datetime):
#         """Test de au_revoir pendant la nuit"""
#         mock_datetime.datetime.now.return_value = datetime(2024, 1, 1, 23, 0, 0)  # 23h
#         with patch("builtins.print") as mock_print:
#             au_revoir()
#             mock_print.assert_called_with("Bonne nuit!")  # Vérifie le message "Bonne nuit!"

if __name__ == "__main__":
    unittest.main()
