inp_str = input('Введите последоветельность цифр:')
cnt = [0]*10
for c in inp_str:
    if c.isdigit():
         i = int(c)
         cnt[i] += 1
for i in range(0, 10):
    print(i, cnt[i])
