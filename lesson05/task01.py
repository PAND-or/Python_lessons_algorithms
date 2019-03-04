#!/usr/bin/python3
__author__ = "Андрей Петров"

"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, 
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
Примечание: 4 квартала - это 4 разных прибыли ;-)
"""

from collections import namedtuple


enterprise_count = int(input('Введите кол-во предприятий: '))

New_Enterprise = namedtuple('New_Enterprise', 'name, i_quarter, ii_quarter, iii_quarter, iv_quarter, total')
enterprises = []
result = {
    'avg_value': 0,
    'i_quarter': 0,
    'ii_quarter': 0,
    'iii_quarter': 0,
    'iv_quarter': 0,
    'total': 0,
    'high_avg': [],
    'low_avg': []
}


for i in range(enterprise_count):
    name = input(f'Введите название пердприятия {i+1}: ')
    i_quarter = float(input(f'Введите прибыль первого квартала пердприятия {i+1}: '))
    ii_quarter = float(input(f'Введите прибыль второго квартала пердприятия {i+1}: '))
    iii_quarter = float(input(f'Введите прибыль третьего квартала пердприятия {i+1}: '))
    iv_quarter = float(input(f'Введите прибыль четвертого квартала пердприятия {i+1}: '))

    total = i_quarter + iii_quarter + iii_quarter + iv_quarter

    result['total'] += total
    result['i_quarter'] += i_quarter
    result['ii_quarter'] += ii_quarter
    result['iii_quarter'] += iii_quarter
    result['iv_quarter'] += iv_quarter

    enterprises.append(New_Enterprise(name, i_quarter, ii_quarter, iii_quarter, iv_quarter, total))


result['avg_value'] = result['total'] / enterprise_count


for k, value in enumerate(enterprises):
    if value.total > result['avg_value']:
        result['high_avg'].append(value)
    else:
        result['low_avg'].append(value)


print(f"\n\n Средняя прибыль за год {result['avg_value']}")

print("\nПредприятия с прибылью выше среднего:")
for value in result['high_avg']:
    print(f"{value.name}, прибыль за год {value.total}")

print("\nПредприятия с прибылью Ниже среднего:")
for value in result['low_avg']:
    print(f"{value.name}, прибыль за год {value.total}")