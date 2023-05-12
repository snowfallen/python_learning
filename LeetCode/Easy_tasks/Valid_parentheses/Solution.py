from typing import Dict


class Solution:
    @staticmethod
    def is_valid(brackets_string: str) -> bool:
        brackets_string_dict: Dict = {'(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{'}
        for index in range(0, len(brackets_string)):
            print(brackets_string_dict[str(brackets_string[index])])


Solution.is_valid("()()")
