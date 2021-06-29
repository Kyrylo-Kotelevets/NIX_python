"""
Есть список из случайных чисел и строк. Создайте цикл, итерирующийся до тех пор, пока не встретится число "777".
Если в течении 100 попыток число не будет найдено — остановить цикл и вызвать ошибку с соответсвующим сообщением.
"""

from random import randint

lst = [randint(500, 999) for _ in range(100 + 1)]

ind = 0
while not (isinstance(lst[ind], int) and lst[ind] == 777):
    if ind > 99:
        raise Exception("Maximum number of iterations exceeded")
    ind += 1

print(ind, lst[ind])
