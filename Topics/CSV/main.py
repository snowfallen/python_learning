# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)


# from pandas import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny

# print(type(data["temp"]))
# <class 'pandas.core.series.Series'>

# print(data["temp"])
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24

# print(data.to_dict())
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
# 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain',
# 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

# print(data["temp"].to_list())
# [12, 14, 15, 14, 21, 22, 24]

# print(data["temp"].mean())
# 17.428571428571427

# print(data["temp"].max())
# 24
# print(data["temp"].min())
# 12


# print(data["temp"])
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24
# Name: temp, dtype: int64

# print(data.temp)
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24
# Name: temp, dtype: int64

# print(data.day == "Monday")
# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# 6    False

# print(data[data.day == "Monday"])
#       day  temp condition
# 0  Monday    12     Sunny

# create a DataFrame
# data_frame: dict = {
#     "Students": ['Amy', "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# print(pandas.DataFrame(data_frame))
#   Students  scores
# 0      Amy      76
# 1    James      56
# 2   Angela      65

# data = pandas.DataFrame(data_frame).to_csv("new_csv")
