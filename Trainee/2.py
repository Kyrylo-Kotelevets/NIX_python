"""
Дан список из словарей в формате [{'name': 'Oleg', 'age': 23}, {'name': 'Vasya', 'age': 19}]
Отсортируйте список по возрасту людей, чтобы получилось [{'name': 'Vasya', 'age': 19}, {'name': 'Oleg', 'age': 23}]
Используйте sorted и lambda
"""

lst = [{'name': 'Oleg', 'age': 23},
       {'name': 'Vasya', 'age': 19}]

print(sorted(lst, key=lambda item: item['age']))
