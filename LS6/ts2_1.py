
# Python 3.7 ОС 64
# Расчет памяти
print(f'Память для переменных (байт): {4 * 28}')


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


print(find_prime_factor(1000))
