"""
Создать функцию, которая принимает на вход два списка:
первый — список, который нужно очистить от определённых значений,
второй — список тех значений, от которых нужно очистить.
Например, list1 = [1, 2, 3, 4, 5], list2 = [1, 3, 4], функция должна вернуть [2, 5]
"""

def delete_from_list(lst: list, to_delete: list) -> list:
    """Function clears the first list from the values of the second list

    :param lst: list to clear of certain values
    :param to_delete: list of those values that need to be cleared
    :return: list cleared of the required values
    """
    return [item for item in lst if item not in set(to_delete)]


list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 4]
print(delete_from_list(list1, list2))  # [2, 5]
print(delete_from_list(list2, list1))  # []
