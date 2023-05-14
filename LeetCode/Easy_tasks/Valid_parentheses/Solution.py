from typing import Dict, List


class Solution:
    @staticmethod
    def is_valid(brackets_string: str) -> bool:
        brackets_dictionary: Dict = {'(': ')', '[': ']', '{': '}'}
        stack: List[str] = []
        for bracket in brackets_string:
            if bracket in '([{':
                stack.append(bracket)
            elif len(stack) == 0 or bracket != brackets_dictionary[stack.pop()]:
                return False
        return len(stack) == 0


Solution.is_valid("()(")
