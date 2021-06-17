inp_str = input('Введи целое число:')
odd_, nodd_ = [], []
for c in inp_str:
    if c.isdigit():
         i = int(c)
         if i % 2 == 0:
             odd_.append(i)
         else:
             nodd_.append(i)
print(f'четных = {len(odd_)} : {odd_}')
print(f'нечетных = {len(nodd_)} : {nodd_}')
