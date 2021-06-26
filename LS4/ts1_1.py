import time
import cProfile
import random as rnd
import numpy as np


def helper():
    nn = 500
    min1 = np.array([0 for i in range(0, nn)])
    m = np.array([([rnd.randint(1, 100) for i in range(0, nn)]) for j in range(0, nn)])

#    print(m)

    start = time.time()
    for i in range(0, nn):
        min1[i] = min(m[i, 0: nn])
    print(f'{(time.time() - start) * 1000 }')  #msec

    start = time.time()
    min_ = max(min1)
    print(f'{(time.time() - start) * 1000 }')  #msec

    print(min_)


cProfile.run('helper()')
