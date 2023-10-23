import pandas

student_dict = {
    'names': ['Eisha', 'Fatima', 'Hiba', 'Pareesa', 'Saira', 'Aniya'] ,
    'scores': [50, 53, 56, 67, 45, 64]
}

student_data_frames = pandas.DataFrame(student_dict)
print(student_data_frames)

for (i, r) in student_data_frames.iterrows():
    #print(r)
    if r.scores > 60:
        print(r.names)
