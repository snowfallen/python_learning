def two_smallest_numbers():
     return sum(sorted(number_list2)[:2])
number_list2: int = []
numbers: int = int(input("Enter numbers of elements "))
for i in range (0 , numbers):
        num = int(input())
        number_list2.append(num)   



print(two_smallest_numbers())