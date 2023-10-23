import pandas
data = pandas.read_csv("226 weather-data.csv")
print(data["temp"])
dictionary = data.to_dict()
print(dictionary)
temperature = data["temp"].tolist()
print(temperature)
sum_of_temp = sum(temperature)
avg = sum_of_temp/ len(temperature)
print(round(avg, 2))
average = data["temp"].mean()
print(average)
maximum = data["temp"].max()
print(maximum)
print(data[data.day == "Monday"])
print(data[data.temp == maximum])
monday = data[(data.day == "Monday")]
temp_in_c = monday.temp
temp_in_f = (9/5) * temp_in_c + 32
print(temp_in_f)