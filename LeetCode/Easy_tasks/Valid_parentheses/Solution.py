from typing import Dict, List


class Solution:
    @staticmethod
    def is_valid(brackets_string: str) -> bool:
        brackets_mapping: Dict[str, str] = {'(': ')', '[': ']', '{': '}'}
        stack: List[str] = []
        for bracket in brackets_string:
            if bracket in '([{':
                stack.append(bracket)
            elif len(stack) == 0 or bracket != brackets_mapping[stack.pop()]:
                return False
        return len(stack) == 0


Solution.is_valid("()(")
