from faker import Faker
from tabulate import tabulate
fake = Faker()

table = [['name','adress']]

for i in range(10):
    name = fake.name()
    adress = fake.address()
    table.append([name,adress])
    
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))