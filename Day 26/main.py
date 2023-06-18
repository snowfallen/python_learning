import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # print(value)

student_dataframe = pandas.DataFrame(student_dict)

# print(student_dataframe)

# Looping through dataframe
# for (key, value) in student_dataframe.items():
#     print(value)

# Looping through rows of a data frame
# for (index, row) in student_dataframe.iterrows():
#     if row.student == "Angela":
#         print(row.score)

# TODO:1.Create a dictionary in the format:
#    {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word:").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()












