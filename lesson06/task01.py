#!/usr/bin/python3
__author__ = "Андрей Петров"

"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. 
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
P.S. Напишите в комментариях версию Python и разрядность ОС.
"""

import sys
from types import ModuleType


# import platform
# from distutils import util

# print(sys.version_info)
# sys.version_info(major=3, minor=7, micro=1, releaselevel='final', serial=0)

# python -V
# Python 3.6.5

# print(platform.python_version())
# 3.7.1

# print(sys.platform)
# win32

# print(util.get_platform())
# win-amd64

# print(platform.architecture())
# ('64bit', 'WindowsPE')

"""
Очень странные показатели по версии OS, реально у меня стоит windows10x64, PyCharm так же установлен 64 разрядный, но sys.platform возвращает 32бита. Почему?
Так же если делать кодом версию Python - выдает 3.7.1 а в консоли команда версии выдает Python 3.6.5
"""


def show_size(x, level=0, size=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    size += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size += sys.getsizeof(item)
    return size


def my_vars(keys):
    s = 0
    for v in keys:
        s +=show_size(globals()[v])
    print(f'summ of memory in vars: {s}\n\n')


# print('Подсчет суммы чисел ряда  1 -0.5 0.25 -0.125 ...')
n = 50
summa = 1
x = 1

for i in range(0, n - 1):
    x = x / -2
    summa += x
#print(f'Результат работы программы Сумма: {summa}')


my_vars(['n','summa', 'x'])
"""
type = <class 'int'>, size = 28, object = 50
type = <class 'float'>, size = 24, object = 0.6666666666666661
type = <class 'float'>, size = 24, object = -1.7763568394002505e-15
summ of memory in vars: 76
"""


"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
"""

multiple_count = {}

for i in range(2, 100):
    for j in range(2, 10):
        if (i % j == 0):
            if j not in multiple_count:
                multiple_count[j] = 1
            else:
                multiple_count[j] += 1

#print(multiple_count)

#for i in multiple_count:
    #print(f'Чисел кратных {i} - {multiple_count[i]} шт')


my_vars(['multiple_count'])
"""
type = <class 'dict'>, size = 368, object = {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
	 type = <class 'int'>, size = 28, object = 2
	 type = <class 'int'>, size = 28, object = 49
	 type = <class 'int'>, size = 28, object = 3
	 type = <class 'int'>, size = 28, object = 33
	 type = <class 'int'>, size = 28, object = 4
	 type = <class 'int'>, size = 28, object = 24
	 type = <class 'int'>, size = 28, object = 5
	 type = <class 'int'>, size = 28, object = 19
	 type = <class 'int'>, size = 28, object = 6
	 type = <class 'int'>, size = 28, object = 16
	 type = <class 'int'>, size = 28, object = 7
	 type = <class 'int'>, size = 28, object = 14
	 type = <class 'int'>, size = 28, object = 8
	 type = <class 'int'>, size = 28, object = 12
	 type = <class 'int'>, size = 28, object = 9
	 type = <class 'int'>, size = 28, object = 11
summ of memory in vars: 816
"""


"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
"""


import random
random_list = random.sample(range(0,100), 10)

numers = {
    'max_value': random_list[0],
    'min_value': random_list[0],
    'min_key': 0,
    'max_key': 0,
    'sum': 0
}

#print(random_list)

for k,v in enumerate(random_list):
    if v > numers['max_value']:
        numers['max_key'] = k
        numers['max_value'] = v
    elif v < numers['min_value']:
        numers['min_key'] = k
        numers['min_value'] = v

if numers['min_key']+1 < numers['max_key']:
    for i in random_list[numers['min_key']+1:numers['max_key']]:
        numers['sum'] += i
elif numers['min_key'] > numers['max_key']+1:
    for i in random_list[numers['max_key']+1:numers['min_key']]:
        numers['sum'] += i
else:
    pass
    #print('Между минимальным и максимальным элементом нет чисел')

#print(f'Сумма {numers["sum"]}')
#print(numers)

my_vars(['numers', 'random_list'])

"""
type = <class 'dict'>, size = 240, object = {'max_value': 83, 'min_value': 8, 'min_key': 6, 'max_key': 7, 'sum': 0}
	 type = <class 'str'>, size = 58, object = max_value
	 type = <class 'int'>, size = 28, object = 83
	 type = <class 'str'>, size = 58, object = min_value
	 type = <class 'int'>, size = 28, object = 8
	 type = <class 'str'>, size = 56, object = min_key
	 type = <class 'int'>, size = 28, object = 6
	 type = <class 'str'>, size = 56, object = max_key
	 type = <class 'int'>, size = 28, object = 7
	 type = <class 'str'>, size = 52, object = sum
	 type = <class 'int'>, size = 24, object = 0
 type = <class 'list'>, size = 144, object = [77, 56, 64, 79, 49, 36, 8, 83, 24, 57]
	 type = <class 'int'>, size = 28, object = 77
	 type = <class 'int'>, size = 28, object = 56
	 type = <class 'int'>, size = 28, object = 64
	 type = <class 'int'>, size = 28, object = 79
	 type = <class 'int'>, size = 28, object = 49
	 type = <class 'int'>, size = 28, object = 36
	 type = <class 'int'>, size = 28, object = 8
	 type = <class 'int'>, size = 28, object = 83
	 type = <class 'int'>, size = 28, object = 24
	 type = <class 'int'>, size = 28, object = 57
summ of memory in vars: 1080
"""