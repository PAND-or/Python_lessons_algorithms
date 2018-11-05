#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

matrix = [
    [1,4,5,8],
    [3,2,4,5],
    [5,6,3,8],
    [9,6,5,4],
]

dictnumbers = {}

for j in range(0, len(matrix[0])):
    for i in range(0, len(matrix)):
        if not(j in dictnumbers):
            dictnumbers[j] = {
                'min_value': matrix[i][j],
                'min_row_index': i
            }
        elif matrix[i][j] < dictnumbers[j]['min_value']:
            dictnumbers[j] = {
                'min_value': matrix[i][j],
                'min_row_index': i
            }
    if not('max' in dictnumbers):
        dictnumbers['max'] = {
            'value': dictnumbers[j]['min_value'],
            'row': dictnumbers[j]['min_row_index'],
            'col': j
        }
    elif dictnumbers[j]['min_value'] > dictnumbers['max']['value']:
        dictnumbers['max'] = {
            'value': dictnumbers[j]['min_value'],
            'row': dictnumbers[j]['min_row_index'],
            'col': j
        }
        
print(f"Максимальный элемент среди минимальных элементов столбцов матрицы \n\
      число: {dictnumbers['max']['value']} \n\
      строка {dictnumbers['max']['row']+1}, \n\
      столбец {dictnumbers['max']['col']+1}")