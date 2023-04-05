import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        assert french_to_english("Bonjour") == "Hello"

    def test_english_to_french(self):
        assert english_to_french("Hello") == "Bonjour"

    def test_french_to_english_null_input(self):
        assert french_to_english(None) == ""

    def test_english_to_french_null_input(self):
        assert english_to_french(None) == ""

unittest.main()