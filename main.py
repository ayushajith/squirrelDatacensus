# import csv
"""Instead of using csv use panda"""
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas


# def to_farenhiet(temp):
#     new_temp = (temp * 9 / 5) + 32
#     return new_temp


# data = pandas.read_csv("weather_data.csv")
# max_temp = data.temp.max()
# print(data[data.temp == max_temp]) # Accessing rows

# monday = data[data.day == "Monday"]
# temp_in_farenhiet = to_farenhiet(monday.temp)
# print(temp_in_farenhiet)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_sq_count, red_sq_count, black_sq_count]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")
# print(pandas.DataFrame(data_dict))





