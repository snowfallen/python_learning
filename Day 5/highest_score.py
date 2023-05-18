students_scores: int = input("Input a list of students scores ").split()

for index in range (0, len(students_scores)):
    students_scores[index] = int(students_scores[index])
print(students_scores)

highest_score = 0
for score in students_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
    