class Solution:
    @staticmethod
    def digital_root(number: int) -> int:
        numbers_string: str = str(number)
        sum_numbers: int = 0
        if len(numbers_string) > 1:
            for index, number in enumerate(numbers_string):
                sum_numbers += int(number)
            return Solution.digital_root(sum_numbers)
        else:
            print(number)
            return number


Solution.digital_root(167)