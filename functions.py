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


# def check_capital_letters(sentence):
#     lst = sentence.split(". ")
#     for l in lst:
#         print(l,l[0].isupper())
#     return ". ".join(list(map(lambda i: i.capitalize() if not i.istitle() else i, lst)))
