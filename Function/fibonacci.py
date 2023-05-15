number_list: int = []

for index in range (0, 10):
    if len(number_list) == 0:
        number_list.append(1)
    if len(number_list) == 1:
        number_list.append(number_list[index] + number_list[index])
    else:
        number_list.append(number_list[index - 1] + number_list[index])
        

print(index)
