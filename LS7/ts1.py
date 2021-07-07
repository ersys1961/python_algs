import random as rnd


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        f_inverse = False
        for i in range(len(arr)-n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                f_inverse = True
        if not f_inverse:  # Прекращаем итерации дострочно если не было перестановок
            break
        n += 1
    return arr


arr1 = [rnd.randint(-100, 100) for i in range(0, 30)]
print(arr1)
print(bubble_sort(arr1))
