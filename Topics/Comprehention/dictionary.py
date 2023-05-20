from random import randrange

user_dict: dict[str: int] = {'Alex': 25, 'Max': 23, 'Vlad': 24, 'Masha': 21, 'Vicki': 21}
# print(user_dict)
# {1: 'Alex', 2: 'Max', 3: 'Vlad', 4: 'Masha', 5: 'Vicki'}

# new_user_dict: dict[str, int] = {key: name for (key, name) in user_dict.items()}
# print(new_user_dict)
# {'Alex': 25, 'Max': 23, 'Vlad': 24, 'Masha': 21, 'Vicki': 21}

user_name_list: list[str] = ['Alex', 'Max', 'Vlad', 'Masha', 'Vicki']
# user_name_dict: dict[int, str] = {randrange(0, 10): name for name in user_name_list}
# print(user_name_dict)
# {9: 'Alex', 2: 'Max', 7: 'Vlad', 4: 'Masha', 1: 'Vicki'}

# user_name_dict: dict[int, str] = {randrange(0, 10): name for name in user_name_list if name != 'Vicki'}
# print(user_name_dict)
# {1: 'Alex', 5: 'Max', 2: 'Vlad', 6: 'Masha'}

