import random as rnd
min_neg = -9999999999999
n = 100
arr1 = [rnd.randint(-100, 100) for i in range(1, n + 1)]
print(arr1)
max_e = min_neg
max_i, idx = 0, 0
for elem in arr1:
    if 0 > elem > max_e:
        max_e = elem
        max_i = idx
    idx += 1
if max_e != min_neg:
    print(f'Позиция {max_i}, значение {max_e}')
else:
    print('отсутствует.')
