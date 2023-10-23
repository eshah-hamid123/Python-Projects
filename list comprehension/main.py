numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Eisha"
temp = [letter for letter in name]
print(temp)

multiples = [n*2 for n in range(1, 5)]
print(multiples)

names = ['Eisha', 'Fatima', 'Hiba', 'Pareesa', 'Saira', 'Aniya']
short_listed_names = [n for n in names if len(n) < 6]
print(short_listed_names)
upper_case_names = [n.upper() for n in names if len(n) >= 6]
print(upper_case_names)
