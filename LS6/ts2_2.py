#  Python 3.7 ОС 64
# Расчет размера памяти для переменных
print(f'Память для списка lst (байт): {40 + 1000 * 8 * 8}')
print(f'Память для других переменных (байт): {8 * 28}')

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
    print(f' ??? lst.__sizeof__() = {lst.__sizeof__()}')
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


print(find_prime_factor(1000))
