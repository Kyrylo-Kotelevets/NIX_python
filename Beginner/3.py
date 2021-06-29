"""
Напишите функцию, которая будет преобразовывать цену к формату, отображающему до двух знаков после точки, например:
22.32131 -> 22.32
58.60125 -> 58.6
34.0 -> 34
"""


def round_price(price: float) -> float:
    """This function converts the price to a format that displays up to two decimal places.
    A number without a fractional part is converted to an integer.

    :param price: float number
    :return: price rounded to two decimal places max
    """
    if not price % 1:  # If number don`t have fractional part
        return int(price)
    return round(price, 2)


print(round_price(22.32131))
print(round_price(58.60125))
print(round_price(34.0))
