# Using pandas to help with CSV files
# https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/reference/index.html

"""
NOTE:
    In Pandas:
    1. The whole table reference as  data frame
    2. Each column of the table reference as series
"""
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print("-------------")
# # Convert it into a dictionary
# data_dict = data.to_dict()
# print(data_dict)
# print("-------------")
# # Convert the data series to a python list
# temp_list = data["temp"].to_list()
# print(f"Temperature list: {temp_list}")
# print("-------------")
#
# # The mean of the temperature
# print(f"Average Temperature: {data["temp"].mean()}")
# # The max of the temperature
# print(f"Maximum Temperature: {data["temp"].max()}")
# print("=============================================")
#
# # Get Data in Columns
# """
# Either code works (Case sensitive)
# """
# print(data["condition"])
# print(data.condition)
# print("-------------")
#
# # Get Data in row
# """
# Either code works (Case sensitive)
# 1.tap into the column
# 2. check the row in the column  for the value that is equal to the one you want
# """
# print(data[data.day == "Monday"])

# Get the row of the highest temperature
# print(data[data.temp == data.temp.max()])  # data[condition]

# Get the particular row's condition
monday = data[data.day == "Monday"]
temperature = monday.temp
converted_temp = temperature * (9 / 5) + 32
print(converted_temp)

# # Create a dataframe from scratch
# data_dict = {
#     "student": ["Andy", "Qiyang", "Jerene", "ShiYing", "JianHao"],
#     "Score": [100, 90, 80, 70, 60]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

