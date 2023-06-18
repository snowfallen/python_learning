import csv

# with open("weather_data.csv", "r") as weather_data:
#     weather_days = weather_data.readlines()
#     print(weather_days)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# Convert Celsius in Fahrenheit
# monday_temp = monday.temp
# monday_temp_F = int(monday_temp) * 9/5 + 32
# print(monday_temp_F)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data_csv")
print(data)