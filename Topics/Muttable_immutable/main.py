# immutable
# None
# bool
# int
# str
# tuple

# mutable
# list
# dict
# set

# x: int = 5
# print(id(x))
# 4310899448
# x: int = 10
# print(id(x))
# 4319878040

my_str: str = "Hello worlf"
# my_str[-1] = 'd'
# TypeError: 'str' object does not support item assignment

my_str2 = my_str
# print(id(my_str))
# 4343124656
# print(id(my_str2))
# 4343124656

# print(my_str is my_str2)
# True

my_str += '!'


