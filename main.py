
letter_list = ["a", "b", "c", "d"]

number_list = []


for index in range (0, 10):
    if len(number_list) == 0:
        number_list.append(1)
    if len(number_list) == 1:
        number_list.append(number_list[index] + number_list[index])
    else:
        number_list.append(number_list[index - 1] + number_list[index])
        

print(index)




def two_smallest_numbers():
     return sum(sorted(number_list2)[:2])
number_list2 = []
numbers = int(input("Enter numbers of elements "))
for i in range (0 , numbers):
        num = int(input())
        number_list2.append(num)   
print(number_list2)


print(two_smallest_numbers())

    

        

    
    


# 1 1 2 3 5 8 