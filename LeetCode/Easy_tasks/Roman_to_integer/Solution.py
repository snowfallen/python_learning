from typing import Dict


class Solution:
    @staticmethod
    def roman_to_int(roman_string_numbers: str) -> int:
        roman_numbers: Dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer_numbers: int = 0
        for index in range(0, len(roman_string_numbers)):
            if roman_numbers[roman_string_numbers[index]] < roman_numbers[roman_string_numbers[index + 1]]:
                integer_numbers -= roman_numbers[roman_string_numbers[index]]
            else:
                integer_numbers += roman_numbers[roman_string_numbers[index]]

        return integer_numbers + roman_numbers[roman_string_numbers[-1]]


Solution.roman_to_int('MCMXCIV')