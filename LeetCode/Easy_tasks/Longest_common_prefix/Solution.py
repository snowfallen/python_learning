from typing import List


class Solution:
    @staticmethod
    def longest_common_prefix(str_list: List[str]) -> str:
        longest_prefix: str = ''
        for letter in zip(*str_list):
            if len(set(letter)) == 1:
                longest_prefix += letter[0]
            else:
                break

        return longest_prefix


Solution.longest_common_prefix(["flower", "flow", "flight"])