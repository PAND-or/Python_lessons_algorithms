#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

while True:
    inp = input('Напишите трехзрачное число: ')
    
    if(len(inp) == 3) & (int(inp) > 100):
        summ = 0
        eq = 1
        
        for i in inp:
            summ += int(i)
            eq = eq * int(i)
            
        print('Сумма чисел: {}, произведение чисел: {}'.format(summ, eq))
        break
        
    else:
        print('Не трехзначное число, повторите ввод')
        inp = input('Напишите трехзрачное число: ')