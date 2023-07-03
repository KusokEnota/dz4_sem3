""" 2 . Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента.
(речь идет про **kwargs)"""


def somefunc(**kwargs):
    mydict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            value = str(value)
        mydict[value] = key
    return mydict


print(somefunc(a=777, b='Hi', c=20.99, d=[2, 3, 4, 5, 6, 7], e={99, 100, 101}, g=(1, 2, 3, 4, 5)))
