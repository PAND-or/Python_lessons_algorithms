#!/usr/bin/python3
__author__ = "Андрей Петров"


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

print(random_list)

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
    print('Между минимальным и максимальным элементом нет чисел')

print(f'Сумма {numers["sum"]}')
print(numers)