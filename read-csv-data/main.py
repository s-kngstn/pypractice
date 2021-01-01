# CSV = Comma Seperated Values

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # average_temp = round(sum(temp_list) / len(temp_list), 2)
# # print(average_temp)
#
# average_temp = data["temp"].mean()
# # .mean() prints the average
# print(average_temp)
#
# max_temp = data["temp"].max()
# # .max() get the max number from the data series
# print(max_temp)
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
# print(data.temp)

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.condition == "Sunny"])

# Create a Dataframe from scratch
# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
#
# more_data = pandas.DataFrame(data_dict)
# more_data.to_csv("more_data.csv")
# print(more_data)

# REMEMBER YOU CAN USE THE len() FUNCTION ON DATA
squirrel_data = pandas.read_csv("squirrel_data.csv")

squirrel_fur_color = squirrel_data["Primary Fur Color"].to_list()
g_amount = squirrel_fur_color.count("Gray")
r_amount = squirrel_fur_color.count("Cinnamon")
b_amount = squirrel_fur_color.count("Black")

squirrel_count = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [g_amount, r_amount, b_amount]
}

squirrel_dataframe = pandas.DataFrame(squirrel_count)
squirrel_dataframe.to_csv("squirrel_count.csv")
print(squirrel_dataframe)
