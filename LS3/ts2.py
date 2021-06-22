arr1 = [8, 3, 15, 6, 4, 2]
arr2 = []
idx = 0
for elem in arr1:
    if elem % 2 == 0:
        arr2.append(idx)
    idx += 1
print(arr2)
