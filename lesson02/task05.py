#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

def row_construct(t, r):
    pattern = '| {:<3}: {:<2} ' * r + '|'
    return  pattern.format(*t)

def rowchar(s, e, r):
    row = []
    result = ''
    for i in range(s, e):
        row.append(i)
        row.append(chr(i))
        if len(row) >= r*2:
            result += row_construct(tuple(row), r) + '\n'
            row = []
    if len(row) > 0:
        result += row_construct(tuple(row), len(row) // 2) 
    return result
print(rowchar(32, 127, 10))