# функция is_prime имеет сложность O(n**1/2)
# функция find_prime_factor  - ?


import time


def is_prime(num):
    """Проверка является ли число простым"""
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def find_prime_factor(num):
    """Найти n - е простое число"""
    cnt = 0
    nn = 2
    while True:
        if is_prime(nn):
            cnt += 1
            if cnt >= num:
                break
        nn += 1
    return nn


start = time.time()
print(f'{find_prime_factor(1000)}')
print(f'{(time.time() - start) * 1000}')  # msec
#for j in range(3, 1001, 10):
#    print(f'{j} {find_prime_factor(j)}')

