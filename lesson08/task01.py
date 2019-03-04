#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N. 
Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке. 
Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()
"""

from collections import defaultdict


def find_substr(s):
    hash_dict = defaultdict(int)
    str_len = len(s)
    summ = 0
    for n in range(1, str_len): # последовательное увеличение длинны подстроки
        for i in range(str_len - n + 1):  # сдвиг каретки для взятия подстроки
            sub = hash(s[i:i+n])
            if sub not in hash_dict:  # Если подстрока встретилась первый раз
                for j in range(str_len - n + 1):  # сдвиг каретки для поиска подстроки
                    if sub == hash(s[j:j+n]):
                        hash_dict[sub] += 1
                        summ += 1
    return len(hash_dict), summ


my_string = 'beep boop beer'
res = find_substr(my_string)
print(f'Кол-во уникальных подстрок {res[0]}, кол-во найденных подстрок {res[1]}')
