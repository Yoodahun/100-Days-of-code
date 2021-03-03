# data = []
#
# with open("weather_data.csv") as weather_data:
#     data.append(weather_data.readlines())
#
# print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

data_dic = data.to_dict()
print(data_dic)

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.temp.max())

print(data[data["temp"] == data["temp"].max()]["condition"])