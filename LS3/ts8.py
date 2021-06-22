import random as rnd
m = []
for i in range(0, 5):
  arr1 = [rnd.randint(1, 10) for i in range(0, 4)]
  m.append(arr1)

for el in m:
    sum1 = 0
    for i in range(0, 3):
        sum1 += el[i]
    el[3] = sum1
for el in m:
  print(el)
