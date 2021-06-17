# адгоритм ищет последнее максимальное, если несколько одинаковых максимальных
nums = [12245, 59833, 694448,  12344, 6995]
max_s = 0
for num in nums:
    rest = num
    sum_c = 0
    while rest > 0:
        sum_c += rest % 10
        rest = rest // 10
    if sum_c > max_s:
        max_n = num
        max_s = sum_c
print(f'Максимальная сумма {max_s} для числа {max_n}')