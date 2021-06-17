# Проверим для любого n меньще заданного
n = int(input('Введи целое n:'))
good = True
for i in range(1, n + 1):
    sum1 = sum(k for k in range(1, i + 1))
    if sum1 != i * (i + 1) / 2:
        good = False
        print(f'Для n = {i} правило не верно.')
if good:
    print(f'Для всех n <={n} правило верно.')
