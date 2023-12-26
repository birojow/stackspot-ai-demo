class RomanNumeral:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        elif isinstance(value, str):
            self.value = self._from_roman(value)
        else:
            raise TypeError("Value must be an integer or a string representing a Roman numeral.")

    def as_roman(self):
        return self._to_roman(self.value)

    def as_arabic(self):
        return self.value

    @staticmethod
    def _to_roman(number):
        roman_numerals = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
            50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        result = ""
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            while number >= value:
                result += numeral
                number -= value
        return result

    @staticmethod
    def _from_roman(roman):
        roman_numerals = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
            'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }
        index = 0
        number = 0
        while index < len(roman):
            if (index + 1 < len(roman)) and (roman[index:index+2] in roman_numerals):
                number += roman_numerals[roman[index:index+2]]
                index += 2
            else:
                number += roman_numerals[roman[index]]
                index += 1
        return number
