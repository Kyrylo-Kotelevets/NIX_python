"""
есть 2 списка:
list1 = ['Oleg', 'Vasya', 'Anna']
list2 = ['Ivanov', 'Sidorov', 'Petrova']
используя zip соедините 2 списка так, чтобы получился
список из tuple, в формате [('Oleg', 'Ivanov'), .....]
"""

list1 = ['Oleg', 'Vasya', 'Anna']
list2 = ['Ivanov', 'Sidorov', 'Petrova']

result = list(zip(list1, list2))
print(result)
