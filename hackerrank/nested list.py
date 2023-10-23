nested_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student_data = [name, score]
    nested_list.append(student_data)

min = 1000
sec_min = 1000
for lst in nested_list:
    if lst[1] < min:
        sec_min = min
        min = lst[1]
    elif lst[1] == min:
        pass
    elif lst[1] < sec_min:
        sec_min = lst[1]

names = []
for score in nested_list:
    if score[1] == sec_min:
        names.append(score[0])

final_names = sorted(names)
for name in final_names:
    print(name)
