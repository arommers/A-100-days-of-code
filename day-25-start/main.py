# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     next(data)
# #     temperatures =[]
# #     for row in data:
# #         temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# data_dic = data.to_dict()
# # print(data_dic)
#
# # temp_list = data["temp"].tolist()
# # print(temp_list)
# # average_temp = int(sum(temp_list) / len(temp_list))
# # print(average_temp)
#
# # print(data["temp"].mean())
# # print(data.temp.max())
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_f_temp = monday_temp * 9/5 + 32
# # print(monday_temp)
# # print(monday_f_temp)
#
# data_dict = {
#     "names": ["Amy", "Adam", "Rachel"],
#     "scores": [8, 7, 10],
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_csv_file")
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240703.csv")
color_counts = data["Primary Fur Color"].value_counts()
print(color_counts)

color_counts_df = color_counts.reset_index()
color_counts_df.to_csv("squirrel_count")