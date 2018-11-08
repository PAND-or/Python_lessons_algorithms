#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
random_list = random.sample(range(0,100), 10)

# Минимальное и максимальное значение по дефолту - первый элемент списка
k_min = k_max = 0
v_min = random_list[0]
v_max = random_list[0]

print(f'{"random list":17} {random_list}')

for k, v in enumerate(random_list): # определение минимального и максимального числа
    if(v > v_max):
        v_max = v
        k_max = k
    if(v < v_min):
        v_min = v
        k_min = k

random_list[k_min], random_list[k_max] = random_list[k_max], random_list[k_min]

print(f'{"reverse max & min":17} {random_list}')