import random as rm
num = rm.randint(1, 100)
attempt = 0
print("Угадай число от 0 до 100")
while attempt < 10:
    inp_num = int(input("? Число:"))
    if inp_num > num:
        print("Загаданное число меньше.")
    elif inp_num < num:
        print("Загаданное число больше.")
    else:
        print("Угадал!")
        break
    attempt += 1
if attempt >= 10:
    print(f'Правильный ответ {num}')
