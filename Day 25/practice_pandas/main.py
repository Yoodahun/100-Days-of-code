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

############################################################
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# data_dic = data.to_dict()
# print(data_dic)
#
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # print(data.temp.max())
#
# print(
#     data[data["temp"] == data["temp"].max()]["condition"]
# )
############################################################

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

print(len(grey_squirrels))
print(len(red_squirrels))
print(len(black_squirrels))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(grey_squirrels), len(red_squirrels), len(black_squirrels)]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")









