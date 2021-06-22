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
if min_i != max_i:
    arr1[min_i], arr1[max_i] = arr1[max_i], arr1[min_i]
print(arr1)
