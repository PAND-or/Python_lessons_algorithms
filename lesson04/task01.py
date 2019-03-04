#!/usr/bin/python3
__author__ = "Андрей Петров"

"""
1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания первых трех уроков.
"""
import cProfile
import random


def multiple_count_fn(end):
    """
     hw3 task02 В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
    """

    multiple_count = {}

    for i in range(2, end):
        for j in range(2, 10):
            if (i % j == 0):
                if j not in multiple_count:
                    multiple_count[j] = 1
                else:
                    multiple_count[j] += 1

    return multiple_count


def minmax_matrix(n):

    """
    9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
    """
    def _generate_matrix(n):
        return [[random.randint(-n, n) for _col in range(n)] for _row in range(n)]



    def _find_minmax(matrix):
        dictnumbers = {}
        for j in range(0, len(matrix[0])):
            for i in range(0, len(matrix)):
                if not (j in dictnumbers):
                    dictnumbers[j] = {
                        'min_value': matrix[i][j],
                        'min_row_index': i
                    }
                elif matrix[i][j] < dictnumbers[j]['min_value']:
                    dictnumbers[j] = {
                        'min_value': matrix[i][j],
                        'min_row_index': i
                    }
            if not ('max' in dictnumbers):
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
        return dictnumbers

    matrix = _generate_matrix(n)
    resnumbers = _find_minmax(matrix)

    print(f"Максимальный элемент среди минимальных элементов столбцов матрицы \n\
          #число: {resnumbers['max']['value']} \n\
          #строка {resnumbers['max']['row']+1}, \n\
          #столбец {resnumbers['max']['col']+1}")

    return resnumbers


if __name__ == "__main__":

    # cProfile.run('multiple_count_fn(100)') 1    0.000    0.000    0.000    0.000 task01.py:10(multiple_count_fn)
    # cProfile.run('multiple_count_fn(1000)') 1    0.004    0.004    0.004    0.004 task01.py:10(multiple_count_fn)
    # cProfile.run('multiple_count_fn(10000)') 1    0.045    0.045    0.045    0.045 task01.py:10(multiple_count_fn)
    # cProfile.run('multiple_count_fn(100000)') 1    0.376    0.376    0.376    0.376 task01.py:10(multiple_count_fn)

    # "task01.multiple_count_fn(100)"
    # 100 loops, best of 3: 234 usec per loop

    # "task01.multiple_count_fn(1000)"
    # 100 loops, best of 3: 2.22 msec per loop

    # "task01.multiple_count_fn(10000)"
    # 100 loops, best of 3: 25.7 msec per loop

    # "task01.multiple_count_fn(100000)"
    # 100 loops, best of 3: 261 msec per loop

    """
    Алгоритм выше выполняется с линейной сложностью, время на выполнение алгоритма растет линейно, 
    т.к. основной массив данных функция проходит за один цикл
    """

    # cProfile.run('minmax_matrix(10)')
    # 1    0.000    0.000    0.002    0.002 task01.py:29(minmax_matrix)
    # 1    0.000    0.000    0.000    0.000 task01.py:39(_find_minmax)

    # cProfile.run('minmax_matrix(100)')
    # 1    0.000    0.000    0.209    0.209 task01.py:29(minmax_matrix)
    # 1    0.004    0.004    0.004    0.004 task01.py:39(_find_minmax)

    # cProfile.run('minmax_matrix(1000)')
    # 1    0.000    0.000   18.941   18.941 task01.py:29(minmax_matrix)
    # 1    0.610    0.610    0.612    0.612 task01.py:39(_find_minmax)

    # "task01.minmax_matrix(10)"
    # 100 loops, best of 3: 373 usec per loop

    # "task01.minmax_matrix(100)"
    # 100 loops, best of 3: 54.8 msec per loop

    # "task01.minmax_matrix(1000)"
    # 100 loops, best of 3: 3.97 sec per loop

    """
       Алгоритм выше выполняется с сложностью близкой к O(N**2) так как строится матрица n на n 
       основной поиск в матрице, практически не занял времени но и он подвержен сложности O(N**2), 
       при увеличении разряда матрицы в 10 раз, время увеличилось на 2 порядка (в 100 раз)
   """
