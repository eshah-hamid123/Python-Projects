import pandas
data_dict = {
    "students": ["Emily", "Rachel", "Matt"],
    "grades": [20, 25, 23]
}
data_of_students = pandas.DataFrame(data_dict)
print(data_of_students)
data_of_students.to_csv("grades.csv")