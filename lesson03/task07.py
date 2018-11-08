#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random
random_list = random.sample([i for i in range(0,100)] * 10, 20) #генерация случайного массива с повторяющимися числами

print(random_list)

numers = {}

for k,v in enumerate(random_list):
    if 'min_first_value' not in numers:
        numers['min_first_value'] = v
    elif v < numers['min_first_value']:
        numers['min_second_value'] = numers['min_first_value']
        numers['min_first_value'] = v
    elif 'min_second_value' not in numers:
        numers['min_second_value'] = v
    elif v < numers['min_second_value']:
        numers['min_second_value'] = v
        
print(f"Два наименьших числа {numers['min_first_value']} и {numers['min_second_value']}")