#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

def recsum(n, z=0):
    if (n < 10): #базовый случай
        z += n
        return int(z)
    else: #Шаг рекурсии 
        z += int(n % 10)
        return recsum(n // 10, z)

max_sum = 0
max_int = 0
print('Подсчет суммы цифр числа и нахождение большей, для завершения введите "exit"')
while True:
    a = int(input('Число: '))
    if a == 'exit':
        break
    sum_a = recsum(a)
    if(max_sum < sum_a):
        max_sum = sum_a
        max_int = a
    print(f'Максимальная сумма {max_sum}, максимальное число {max_int}')
    