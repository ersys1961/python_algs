#  Задача 9 из Задания 3
# Сложность квадратичная O(n**2).
# Так как наибольшее чисто операций в поиске минимума в столбце,
# для каждого из n столцов нужен перебор n элементов.

import cProfile
import random as rnd
import time


def helper():
    m = []
    nn = 500
    min1 = [0 for i in range(0, nn)]
    for j in range(0, nn):
        arr1 = [rnd.randint(1, 100) for i in range(0, nn)]
        m.append(arr1)

    start = time.time()
    for i in range(0, nn):
        min1[i] = m[0][i]
        for j in range(0, nn):
            if min1[i] > m[j][i]:
                min1[i] = m[j][i]

    print(f'{(time.time() - start) * 1000 }')  #msec

    start = time.time()
    min_ = min1[0]
    for el in min1:
        if min_ < el:
            min_ = el
    print(f'{(time.time() - start) * 1000 }')  #msec

    print(min_)


cProfile.run('helper()')
