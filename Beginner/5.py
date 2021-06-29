"""
Напишите функцию, которая принимает список, и число.
Функция должна разбить список на N кусков, переданных в функцию в качестве втрого аргумента.
Выполнить проверки по здравому смыслу (например, нет смысла пытаться разбить список из 3 элементов на 4 элемента)
"""


def clean_slice_list(lst: list, num_piece: int) -> list:
    """Function divides the list into n parts

    :param lst: list with any elements
    :param num_piece: divisor of input array length
    :return: list of slices
    """
    if num_piece < 1 or num_piece > len(lst) or len(lst) % num_piece:
        raise ValueError("Cannot split list with length {} into {} pieces".format(len(lst), num_piece))

    slice_size = len(lst) // num_piece
    return [lst[i * slice_size:(i + 1) * slice_size] for i in range(num_piece)]


def slice_list(lst: list, num_piece: int) -> list:
    """The function divides the list into n parts,
    if the list is not a multiple of n, then add the remaining elements to the last slice

    :param lst: list with any elements
    :param num_piece: positive integer smaller than list length
    :return: list of slices
    """
    if num_piece < 1 or num_piece > len(lst):
        raise ValueError("Cannot split list with length {} into {} pieces".format(len(lst), num_piece))

    slice_size = len(lst) // num_piece
    result = [lst[i * slice_size:(i + 1) * slice_size] for i in range(num_piece)]

    tail = len(lst) % num_piece
    if tail:  # If there are elements left, add them to the last slice
        result[-1] += lst[-tail:]

    return result


def module_slice_list(lst, num_piece):
    """Function divides the list into n parts by remainder of n

    :param lst: list with integers
    :param num_piece: positive integer smaller than list length
    :return: list of slices
    """
    if num_piece < 1 or num_piece > len(lst):
        raise ValueError("Cannot split list with length {} into {} pieces".format(len(lst), num_piece))

    # We group the elements by their remainders after division by n
    return [[lst[i] for i in range(len(lst)) if (i % num_piece) == r] for r in range(num_piece)]


lst = list(range(10))
print(clean_slice_list(lst, 3))  # ValueError
print(slice_list(lst, 3))  # [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]
print(module_slice_list(lst, 3))  # [[0, 3, 6, 9], [1, 4, 7], [2, 5, 8]]
