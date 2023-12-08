import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231207.csv")
g_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(g_squirrels_count)

b_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(b_squirrels_count)

c_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(c_squirrels_count)

all_squirrels_count = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [g_squirrels_count, b_squirrels_count, c_squirrels_count]

}

new_data = pandas.DataFrame(all_squirrels_count)
new_data.to_csv("new_data.csv")
