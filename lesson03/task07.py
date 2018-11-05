#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random
random_list = random.sample([i for i in range(0,100)] * 10, 20) #генерация случайного массива с повторяющимися числами

numers = {
    'min_first_value': random_list[0],
    'min_second_value': random_list[0],
}

print(random_list)

for k,v in enumerate(random_list):
    if v <= numers['min_first_value']:
        numers['min_second_value'] = numers['min_first_value']
        numers['min_first_value'] = v
        
print(f"Два наименьших числа {numers['min_first_value']} и {numers['min_second_value']}")