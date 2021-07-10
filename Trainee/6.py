"""
Дан список из словарей:
list_ = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Oleg', 'age': 23},
    {'name': 'Anna', 'age': 32},
    {'name': 'Igor', 'age': 50},
    {'name': 'Anton', 'age': 17},
]
Отфильтруйте его так, чтобы в нём остались только люди, имена которых
начинаются с буквы "А", и возраст между 18 и 30 годами включительно.
В итоговом результате должен быть такой список:
[{'name': 'Alex', 'age': 25}]
"""

list_ = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Oleg', 'age': 23},
    {'name': 'Anna', 'age': 32},
    {'name': 'Igor', 'age': 50},
    {'name': 'Anton', 'age': 17},
]

pattern = lambda record: record['name'].startswith('A') and (18 <= record['age'] <= 30)
list_ = list(filter(pattern, list_))
print(list_)
