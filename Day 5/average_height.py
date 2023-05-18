students_heights: int = input("Input a list of students heights ").split()

for index in range (0,len(students_heights)):
    students_heights[index] = int(students_heights[index])
print(students_heights)

total_height: int = 0
for height in students_heights:
    total_height = total_height + height
# print(total_height)

number_of_students: int = 0
for student in students_heights:
    number_of_students += 1
# print(number_of_students)

average_height: int = round(total_height / number_of_students)
print(average_height) 
 