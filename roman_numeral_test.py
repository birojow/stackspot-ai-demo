import unittest

# Assuming the RomanNumeral class is defined in roman_numeral.py
from roman_numeral import RomanNumeral

class RomanNumeralTest(unittest.TestCase):
    def test_should_create_roman_numeral_object_from_int(self):
        actual_numerals = [RomanNumeral(i).as_roman() for i in [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
            200, 300, 400, 500, 600, 700, 800, 900, 1000
        ]]
        expected_numerals = [
            "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XX",
            "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C", "CC", "CCC", "CD", "D",
            "DC", "DCC", "DCCC", "CM", "M"  # Corrected "DCCCC" to "CM"
        ]
        self.assertListEqual(expected_numerals, actual_numerals)

    def test_should_create_roman_numeral_object_from_string(self):
        actual_numerals = [RomanNumeral(s).as_arabic() for s in [
            "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XX",
            "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C", "CC", "CCC", "CD", "D",
            "DC", "DCC", "DCCC", "CM", "M"  # Assuming "CM" is the correct representation for 900
        ]]
        expected_numerals = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
            200, 300, 400, 500, 600, 700, 800, 900, 1000
        ]
        self.assertListEqual(expected_numerals, actual_numerals)

if __name__ == '__main__':
    unittest.main()
