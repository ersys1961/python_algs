import random as rnd

arr = [rnd.randint(0, 1000) for i in range(0, 31)]
arr1 = sorted(arr)
mid = arr1[15]
print(arr1)
print(mid)