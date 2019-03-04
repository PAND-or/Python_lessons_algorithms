#!/usr/bin/python3
__author__ = "Андрей Петров"

"""
2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.
"""

import cProfile


def erasfen_sieve(n):
    countnaturals = 1
    def _sieve(start, end, res = []):

        sieve = [i for i in range(end)]

        sieve[1] = 0 if sieve[1] == 1 else sieve[1]

        for i in range(start, end):

            if sieve[i] != 0:
                j = i + i
                while j < end:
                    sieve[j] = 0
                    j += i

        return [i for i in sieve if i != 0]

    def _check_sieve(z): # Перебор интервала
        i = len(str(z)) # начальный порядок числа
        while True:
            size = 10**i
            result = _sieve(2, size)
            if len(result) > z:
                break
            i += 1

        return result[z -1]
    res = _check_sieve(n)

    return res

def find_naturals(n):

    count = 1
    k = 2

    while count < n:
        k += 1
        for i in range(2, k):
            if k % i == 0:
                break
        else:
            count += 1

    return k


def test_naturals(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    for i, item in enumerate(lst, start=1):
        assert item == func(i)
        print(f'Test {i} OK')



if __name__ == "__main__":

    # cProfile.run('erasfen_sieve(100)')
    # 1    0.000    0.000    0.001    0.001 task02.py:11(erasfen_sieve)

    # cProfile.run('erasfen_sieve(1000)')
    # 1    0.000    0.000    0.010    0.010 task02.py:11(erasfen_sieve)

    # cProfile.run('erasfen_sieve(10000)')
    # 1    0.027    0.027    0.029    0.029 task02.py:11(erasfen_sieve)

    # cProfile.run('erasfen_sieve(100000)')
    # 1    0.176    0.176   16.482   16.482 task02.py:11(erasfen_sieve)

    # "task02.erasfen_sieve(100)"
    # 100 loops, best of 3: 732 usec per loop

    # "task02.erasfen_sieve(1000)"
    # 100 loops, best of 3: 9.16 msec per loop

    # "task02.erasfen_sieve(10000)"
    # 100 loops, best of 3: 1.42 sec per loop

    # "task02.erasfen_sieve(100000)"
    # 5 loops, best of 3: 14.8 sec per loop

    """
    Решето Эратосфена линейно зависимо от интервала поиска числа, но выбрать верный диапазон у больших чисел сразу не вышло, 
    поэтому свыше 1000 числа наблюдается не линейнее увеличение сложности алгоритма. Есть математический метод для выяснения верного диапазона через число П
    """

    #cProfile.run('find_naturals(10)')
    # 1    0.000    0.000    0.000    0.000 task02.py:43(find_naturals)

    # cProfile.run('find_naturals(100)')
    # 1    0.005    0.005    0.005    0.005 task02.py:43(find_naturals)

    # cProfile.run('find_naturals(1000)')
    # 1    0.873    0.873    0.873    0.873 task02.py:43(find_naturals)

    # cProfile.run('find_naturals(10000)')
    #  1  105.456  105.456  105.456  105.456 task02.py:43(find_naturals)

    # "task02.find_naturals(10)"
    # 100 loops, best of 3: 35.1 usec per loop

    # "task02.find_naturals(100)"
    # 100 loops, best of 3: 4.11 msec per loop

    # "task02.find_naturals(1000)"
    # 100 loops, best of 3: 665 msec per loop

    #print(erasfen_sieve(1))
    #print(find_naturals(1))
    #test_naturals(erasfen_sieve)
    #test_naturals(find_naturals)
    pass
