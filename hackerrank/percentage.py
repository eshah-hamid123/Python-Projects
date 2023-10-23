n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

if query_name in student_marks:
    query_score = student_marks[query_name]
    sum = 0
    for score in query_score:
        sum+= score
    percentage = sum / len(query_score)
    print(f'{percentage:.2f}')

