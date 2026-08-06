import pandas
data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict('records')
# print(data_dict)
# print(data.temp.to_list)
temp_List = data["temp"].to_list()
max_temp = max(temp_List)
print(data[data.temp == max_temp])

print("\n")

import pandas
grey = 0
cinnamon = 0
black = 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260804.csv")
Fur_color_list = data.Primary_Fur_Color.to_list()
for i in Fur_color_list:
    if i == "Gray":
        grey = grey + 1
    elif i == "Cinnamon":
        cinnamon += 1
    elif i == "Black":
        black += 1



print(f"Number of Grey: {grey}\n"
      f"Number of Cinnamon: {cinnamon}\n"
      f"Number of Black: {black}")
