import string
import random
import logging


def key_generator(size=4, chars=string.ascii_letters + string.digits):
    return '#' + ''.join(random.choice(chars) for _ in range(size))


def decor(function):
    def wrapper(*args, **kwargs):
        logging.info(f'Function that {function.__doc__} has started to perform')
        result = function(*args, **kwargs)
        logging.info(f'Function that {function.__doc__} has performed')
        return result

    return wrapper

