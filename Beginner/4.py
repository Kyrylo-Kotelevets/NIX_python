"""
Дан список из строк. Создайте однострочное решение (при помощи list comprehension),
которое приведёт к верхнему регистру все строки, содержащие слово 'price')
"""

strings = ["Given a list of strings",
           "Create a one line solution",
           "(with a list comprehension)",
           "which will convert",
           "all lines containing",
           "the word \'price\'",
           "to uppercase"]

strings = [line.upper() if 'price' in line else line for line in strings]
print(strings)
