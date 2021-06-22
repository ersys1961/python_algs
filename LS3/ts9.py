import random as rnd
m = []
nn = 5
min1 = [0 for i in range(0, nn)]
for j in range(0, nn):
  arr1 = [rnd.randint(1, 100) for i in range(0, nn)]
  m.append(arr1)

for i in range(0, nn):
    min1[i] = m[0][i]
    for j in range(0, nn):
        if min1[i] > m[j][i]:
            min1[i] = m[j][i]

min_ = min1[0]
for el in min1:
    if min_ < el:
        min_ = el

for el in m:
  print(el)
print(min_)
