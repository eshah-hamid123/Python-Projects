import pandas

data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
colors = data["Primary Fur Color"].tolist()
black_count = 0
gray_count = 0
cinnamon_count = 0
for color in colors:
    if color == "Black":
        black_count += 1
    elif color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        cinnamon_count += 1

color_dict = {
    "Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

dict = pandas.DataFrame(color_dict)
dict.to_csv("color_file.csv")



