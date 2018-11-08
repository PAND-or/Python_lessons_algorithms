#!/usr/bin/python3
__author__ = "Андрей Петров"


"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
"""

multiple_count = {}

for i in range(2,100):
    for j in range(2,10):
        if(i % j == 0):
            if j not in multiple_count:
                multiple_count[j] = 1
            else:
                multiple_count[j] += 1

print(multiple_count)
                
for i in multiple_count:  
    print(f'Чисел кратных {i} - {multiple_count[i]} шт')