#  до 999: [2520, 5040, 7560]
l1 = []
for i in range(2, 100):
    Bool = True
    for j in range(2, 10):
        if i % j > 0:
            Bool = False
    if Bool:
        l1.append(i)
print(l1)
