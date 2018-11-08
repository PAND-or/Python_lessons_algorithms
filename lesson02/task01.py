#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""

while True:
    a = int(input('Введите первое число:'))
    operand = input('Операция (0 для выхода):')
    b = int(input('Введите второе число:'))
    if operand == '0':
        print('Пока')
        break
    elif operand == '+':
        print(f'Ответ: {a+b}\n')
    elif operand == '-': 
        print(f'Ответ: {a-b}\n')
    elif operand == '*':
        print(f'Ответ: {a*b}\n')
    elif operand == '/':
        if b == 0:
            print('На 0 делить нельзя!\n')
        else:
            print(f'Ответ: {a/b}\n')
    else:
        print('Не верный знак операции\n')