import os

os.system('cls')


alunas = [
    ('Maria', '2000-10-14', 'A'),
    ('Joana', '1997-08-10', 'A'),
    # ...
]

print(f'{alunas[1][0]} nasceu em {alunas[1][1]}')

print(alunas[1][0] + ' nasceu em ' + alunas[1][1])

print(alunas[1][0], 'nasceu em', alunas[1][1])