list_numbers: list[int] = [1, 2, 3, 4, 5]

square_list_numbers: list[int] = [number ** 2 for number in list_numbers]
# print(square_list_numbers)
# [1, 4, 9, 16, 25]

odd_list_numbers: list[int] = [number for number in list_numbers if number % 2]
# print(odd_list_numbers)
# [1, 3, 5]

even_list_numbers: list[int] = [number for number in list_numbers if not number % 2]
# print(even_list_numbers)
# [2, 4]
