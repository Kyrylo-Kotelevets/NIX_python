"""
Напишите функцию, которая принимает число - таймзону от GMT
(например, Киев - таймзона +2, соответсвенно передаёте 2, или Гавайи - таймзона = -10, соответсвенно передаёте -10),
и возвращает текущую дату и время в указаной таймзоне.
Формат:
[<часов>:<минут>:<секунд>] - <день месяца>, <полное название месяца> of <год>
например: [16:22:26] - 11, March of 2021
"""

from datetime import datetime, timedelta


def current_date(timezone: int=0):
    """Returns current formatted date and time in given timezone """
    res_datetime = datetime.now() + timedelta(hours=timezone)
    return res_datetime.strftime('[%H:%M:%S] - %d, %B of %Y')


print(current_date())
print(current_date(-3))
print(current_date(2))
print(current_date(11))
