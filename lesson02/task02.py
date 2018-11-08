#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

def recursion(n, chet=0, nechet=0):
    if n % 2 == 0:
        chet +=1
    else:
        nechet +=1
    if (n < 10): #базовый случай
        return f'chet={chet}, nechet={nechet}'
    else: #Шаг рекурсии 
        return recursion(n // 10, chet, nechet)

val = input('Введите натуральное число:')
print(recursion(int(val)))