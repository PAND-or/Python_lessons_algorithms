#!/usr/bin/python3
__author__ = "Андрей Петров"


"""

3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

"""

a = input('введите координаты первой точки через запятую x,y: ').split(',')
b = input('введите координаты второй точки через запятую x,y: ').split(',')

A = int(a[1]) - int(b[1])
B = int(b[0]) - int(a[0])
C = int(a[0]) * int(b[1]) - int(b[0]) * int(a[1])

function = '{}x + {}y + {} = 0'.format(A, B, C)
print(function)
    