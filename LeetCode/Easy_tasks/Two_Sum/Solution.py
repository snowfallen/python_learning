from typing import List, Dict

nums: List[int] = [2, 7, 11, 15]


class Solution:
    @staticmethod
    def two_sum(number_list: List[int], target: int) -> List[int]:
        hash_map: Dict[int, int] = {}
        for index, number in enumerate(number_list):
            hold: int = target - number
            if number in hash_map:
                return [hash_map[number], index]
            hash_map[hold] = index


Solution.two_sum(nums, 9)
