"""
Напишите функцию, которая делает return строки приветствия людей
из разных стран на разных языках, в зависимости от страны человека.
Вызовите функцию используя map
Требование: используйте map
Для примера можете взять этот список юзеров:
users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]
На выходе с использованием users_list, после использования map
вы должны получить результат iterable с такими приветствиями:
Привет, Александр!
Hello, James!
Hola, Daniella!
Hello, Someone, but I do not know where are you from!
"""

hello_dict = {
    "ru": "Привет",
    "us": "Hello",
    "es": "Hola"
}


def say_hello(item: tuple) -> str:
    """The function makes a greeting to the user in the specified language

    :param item: tuple with name and language in short lowercase format
    :return: greeting in the specified language
    """
    name, language = item
    hello = hello_dict.get(language)

    if hello is not None:
        return "{}, {}!" . format(hello, name)
    return "Hello, {}, but I do not know where are you from!" . format(name)


users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]
print(list(map(say_hello, users_list)))
