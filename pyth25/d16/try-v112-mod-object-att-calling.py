import prettytable

# create object from class
from prettytable import PrettyTable
table = PrettyTable()

#print bare bone table without data
print(table)
print("____________________________________________________________________")
#create method for adding columns for table fields
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Pokemon Type",["Electric","Water","Fire"])

print(table.align)
print(table)

table.align="l"
print(table.align)

#print the table now with the column data
print(table)