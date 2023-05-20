user_dict: dict[str: int] = {'Alex': 25, 'Max': 23, 'Vlad': 24, 'Masha': 21, 'Vicki': 21}


def fun(**kwargs):
    print(kwargs)
    # print(*kwargs)
    # Alex Max Vlad Masha Vicki


fun(**user_dict)
# {'Alex': 25, 'Max': 23, 'Vlad': 24, 'Masha': 21, 'Vicki': 21}
