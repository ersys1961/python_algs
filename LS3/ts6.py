# предполагется что минимальный и максимальный элементы единственные в массиве
import random as rnd
arr1 = [rnd.randint(1, 200) for i in range(1, 21)]
print(arr1)

min_i, max_i, idx = 0, 0, 0
for e in arr1:
    if e < arr1[min_i]:
        min_i = idx
    if e > arr1[max_i]:
        max_i = idx
    idx += 1
summa = 0
if min_i > max_i:
    min_i, max_i = max_i, min_i
for i in range(min_i + 1, max_i):
    summa += arr1[i]
print(f'мин = {min_i}, макс = {max_i}, сумма= {summa}')

