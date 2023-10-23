# # with open("226 weather-data.csv") as data:
# #     list_of_data = data.readlines()
#     print(list_of_data)
temperature = []
import csv
with open("226 weather-data.csv") as data:
    list_of_data = csv.reader(data)
    for row in list_of_data:
        temp = row[1]
        if temp == "temp":
            pass
        else:
            temp = int(temp)
            temperature.append(temp)
    print(temperature)
    for temp in temperature:
        print(temp)
