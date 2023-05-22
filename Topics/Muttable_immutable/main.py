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

x: str = 'Hello'
# x[-1] = '!'
# Class 'str' does not define '__setitem__', so the '[]' operator cannot be used on its instances
# print(x)


# y: list = [1, 2, 3, 4]
# y.append(5)
# print(y)
# [1, 2, 3, 4, 5]

# create an alias
# z = y

# print(y)
# print(z)
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]

# z.append(0)
# print(z)
# print(y)
# [1, 2, 3, 4, 5, 0]
# [1, 2, 3, 4, 5, 0]

# y.append(9)
# print(z)
# print(y)
# [1, 2, 3, 4, 5, 0, 9]
# [1, 2, 3, 4, 5, 0, 9]

# print(id(y))
# print(id(z))
# 4369552512
# 4369552512

# print(y is z)
# True

print(x)
# Hello

y = x

print(x)
print(y)
# Hello
# Hello

x += '!'
print(x)
# Hello!
print(y)
# Hello

