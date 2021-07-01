# Python 3.7  64 разрядная ОС

arr1 = [8, 3, 15, 6, 4, 2]
arr2 = []
print(f'sizeof arr1 = {arr1.__sizeof__()}')
print(f'подсчет разсмера arr1 = 40 + 8 * 6 = {40 + 8 * 6}')
print(f'пустрой список arr2 {arr2.__sizeof__()}')
idx = 0
size = 0
for elem in arr1:
    if elem % 2 == 0:
        arr2.append(idx)
        size += idx.__sizeof__()   # подсчет в лоб
    idx += 1
print(arr2)
print(f'размер целого = {idx.__sizeof__()}')
print(f'в список arr2 добавили 4 целых элемента = {arr2.__sizeof__()}')
print(f'подсчет длины arr2: 40 + 8 * 4 = {40 + 8 * 4}')
print(size)  # подсчет рамера списка в лоб не работет
