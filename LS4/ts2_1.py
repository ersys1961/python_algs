#  При поиске тысячного числа
#  Время выполнения через проверку числа на "простоту"  - 23 до 35 мксек
#  Время выполения с использованием решета Эратосфена -  от 3 до 6 мксек
#  С использованием решета Эратосфена работает в 6 раз быстрее.
#  Сложность определяется сложность Эратосфена O(log(X))
#  где X - минимальный размер, достаточный для расчета, как функция N.
# Но потребность в памяти растет как O(?) - не знаю как оценить в данном алгоритме
import time
erat_size_mul = 8


def erat(n):
    a = [i for i in range(0, n + 1)]
    a[1] = 0
    k = 2
    while k * k <= n:
        if a[k] != 0:
            for l in range(k * k, n + 1, k):
                a[l] = 0
        k += 1
    return a


def find_prime_factor(num):
    lst = erat(num * erat_size_mul)
    cnt = 0
    found = False
    for i in range(2, len(lst) + 1):
        if lst[i] != 0:
            cnt += 1
            if cnt >= num:
                found = True
                res = lst[i]
                break
    if found:
        return res
    else:
        print(f'Нехватило решета!-) {cnt}')
        return 0


start = time.time()
print(find_prime_factor(1000))
print(f'{(time.time() - start) * 1000}')  # msec