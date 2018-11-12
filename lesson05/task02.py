#!/usr/bin/python3
__author__ = "Андрей Петров"

"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. 
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]. 
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


def my_int(lst):
    dic = {'0': 0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }
    s = 0
    for i, k in enumerate(reversed(lst)):
        s += dic[k] * 16 ** i
    return s


def my_hex(n, s=''):
    dic = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    s += str(dic[n % 16])

    # print(str(int(num % 16)))

    if n < 16:
        return list(reversed(list(s)))
    else:
        return my_hex(int(n // 16), s)


#first_number = list(input('Первое шестнадцатеричное число: '))
#second_number = list(input('Второе шестнадцатеричное число: '))

first_number_dec = my_int(list('A2'))
second_number_dec = my_int(list('C4F'))

summa = my_hex(first_number_dec + second_number_dec)
eqyal = my_hex(first_number_dec * second_number_dec)

print(f'Сумма чисел {summa}, произведение {eqyal}')