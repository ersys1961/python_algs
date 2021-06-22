import random as rnd
arr1 = [rnd.randint(1, 200) for i in range(1, 21)]
print(arr1)

min1_i = 0
for i in range(0, len(arr1)):
    if arr1[i] < arr1[min1_i]:
        min1_i = i

if min1_i != 0:
    min2_i, k = 0, 0
else:
    min2_i, k = 1, 1
for i in range(k, len(arr1)):
    if i != min1_i:
      if arr1[i] < arr1[min2_i]:
          min2_i = i
print(f'мин1 = {min1_i}:{arr1[min1_i]}, мин2 = {min2_i}:{arr1[min2_i]}')
