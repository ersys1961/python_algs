firms = {}
n = int(input("Количество предприятий: "))
profit_all = 0
for i in range(n):
    sname = input(str(i+1) + "-е предприятие: ")
    profit_1 = int(input("Прибыль квартал 1: "))
    profit_2 = int(input("Прибыль квартал 2: "))
    profit_3 = int(input("Прибыль квартал 3: "))
    profit_4 = int(input("Прибыль квартал 4: "))
    profit_y = profit_1 + profit_2 + profit_3 + profit_4
    firms[sname] = profit_y
    profit_all += profit_y

profit_avg = profit_all / n
print("\nСредняя прибыль за год: %.2f'" % profit_avg)
print("\nПредприятия с прибылью выше среднего:")
for key in firms:
    if firms[key] > profit_avg:
        print(key, firms[key])

print("\nПредприятия с прибылью ниже среднего:")
for key in firms:
    if firms[key] < profit_avg:
        print(key, firms[key])
