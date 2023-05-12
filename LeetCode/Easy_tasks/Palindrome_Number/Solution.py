class Solution:
    @staticmethod
    def is_palindrome(number: int) -> bool:
        temp_number: int = number
        reversed_number: int = 0
        while temp_number > 0:
            reversed_number = (reversed_number * 10) + (temp_number % 10)
            temp_number = temp_number // 10

        return number == reversed_number

    # using string
    # def isPalindrome(number: int) -> bool:
    #     return str(number) == str(number)[::-1]


Solution.is_palindrome(12)