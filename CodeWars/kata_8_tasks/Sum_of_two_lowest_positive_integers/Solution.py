from typing import List


class Solution:
    @staticmethod
    def sum_two_smallest_numbers(numbers: List[int]):
        return sum(sorted(numbers)[:2])


Solution.sum_two_smallest_numbers([2, 6, 1, 45])
