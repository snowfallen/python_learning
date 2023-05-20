# def add(first_number: int , second_number: int):
#     return first_number + second_number

# def add(first_number: int, second_number: int, third_number: int):
#     return first_number + second_number + third_number

# def add(first_number: int, second_number: int, third_number: int, ...):
#     return first_number + second_number + third_number + ...
#
# def add(*numbers):
#     sum: int = 0
#     for number in numbers:
#         sum += number
#     return sum
#

# print(add(2, 5, 6, 9))
# 22

# def fun(*numbers):
#     print(numbers)
    # (2, 4, 5, 6)
    # print(*numbers)
    # 2 4 5 6


# print(fun(2, 4, 5, 6))
# (2, 4, 5, 6)

# fun(2, 4, 5, 6)

# def names(*names):
    # print(*names)
    # Alex Max Masha
    # print(names)
    # ('Alex', 'Max', 'Masha')

names_list: list[str] =['Alex', 'Max', 'Masha']
# names('Alex', 'Max', 'Masha')

# names(names_list)
# (['Alex', 'Max', 'Masha'],)

# names(*names_list)
# ('Alex', 'Max', 'Masha')

# names(names_list)

# def names(name, *names):
#     # print(name)
#     # Alex
#     # print(names)
#     # ('Max', 'Masha')
#
# names(*names_list)