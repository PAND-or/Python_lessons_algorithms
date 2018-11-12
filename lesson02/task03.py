#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""

def recursion(n, z=f''):
    if (n < 10): #базовый случай
        z += str(n)
        return int(z)
    else: #Шаг рекурсии 
        z += str(n % 10)
        return recursion(n // 10, z)

val = input('Введите натуральное число:')
recursion(int(val))