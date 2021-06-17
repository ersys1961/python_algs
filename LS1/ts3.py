num = 123456789
num1 = 0
while num > 0:
    rest = num % 10
    num = num // 10
    num1 = num1 * 10 + rest
print(num1)
