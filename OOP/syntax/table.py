from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon_name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'c'
print(table)

