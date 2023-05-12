from typing import Dict


class Solution:
    @staticmethod
    def duplicate_count(text: str) -> int:
        text_to_lower: str = text.lower()
        letter_duplicate: Dict = {}
        for letter in text_to_lower:
            letter_count = text_to_lower.count(letter)
            if letter_count > 1:
                letter_duplicate[letter] = letter_count
        return len(letter_duplicate)


Solution.duplicate_count("abcdeaB")