#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""


import random
random_list = random.sample(range(-100,100), 10)
max_num = {}
print(random_list)

for k,v in enumerate(random_list):
    if v < 0:
        if 'value' not in max_num:
            max_num['key'] = k
            max_num['value'] = v
        elif v > max_num['value']:
            max_num['key'] = k
            max_num['value'] = v

if not('value' in max_num):
    print('Массив не имеет отрицательных значений')
else:
    print(f'Максимальное отрицательное число {max_num["value"]} с индексом {max_num["key"]}') 