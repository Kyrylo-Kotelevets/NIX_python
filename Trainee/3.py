"""
Написать свой декоратор, который будет отлавливать ошибки,
полученные в ходе выполнения обёрнутой функции,
логгировать их и делать raise отловленной ошибки
"""

import logging

logging.basicConfig(filename='app.log', filemode='w', level=logging.ERROR)


def errors_logger(fun):
    """Decorator catches errors for logging"""
    def wrapper(*args):
        try:
            return fun(*args)
        except Exception as error:
            logging.error(error)
            raise error
    return wrapper


@errors_logger
def divide(left, right):
    """Divide function, just for test"""
    return left / right


print(divide(4, 0))
