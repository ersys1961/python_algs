# arr1 - исходный массив,  arr2 - уникальные значеник,  cnt - частотность
import random as rnd
n = 20
arr1 = [rnd.randint(1, 20) for i in range(1, n + 1)]
arr2 = list(set(arr1))
cnt = [0 for i in range(0, len(arr2))]
idx = 0
for e2 in arr2:
    for e1 in arr1:
        if e2 == e1:
            cnt[idx] += 1
    idx += 1
cnt_max = max(cnt)
lst_max = []
for num, cnt_num in zip(arr2, cnt):
    if cnt_max == cnt_num:
        lst_max.append(num)
print(arr1)
print(arr2)
print(cnt)
print(f' макс. частотность {cnt_max} элементы: {lst_max}')
