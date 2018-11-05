#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
4. Определить, какое число в массиве встречается чаще всего.
"""


import random
random_list = random.sample([i for i in range(0,10)] * 10, 20) #генерация случайного массива с повторяющимися числами
print(f'Случайный массив {random_list}')

count = {}
max_nuber = max_count = 0

for i in random_list:
    if(i in count):
        count[i] +=1
    else:
        count[i] = 1
        
    if(count[i] > max_count):
        max_count = count[i]
        max_nuber = i
    
print(f'Больше всех, встречается число: {max_nuber}, вхождений: {max_count}')