#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n – любое натуральное число.
"""

n = int(input('Введите натуральное число: '))
suma = 0

for i in range(n):
    suma += i+1
check = n * (n +1) /2

if(suma == check):
    print('Числа сходятся')
else:
    print('Числа не сходятся')