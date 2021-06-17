import re

while True:
    res = 0
    s = input('Введите числа и операцию. 0-конец работы:')
    if s == '0':
        break
    lst = re.split('[+]|[-]|[*]|[/]', s)
    lst1 = re.findall('[+]|[-]|[*]|[/]', s)
    if len(lst1) > 0:
        opr = lst1[0]
    else:
        opr = '?'
    if len(lst) == 2:
        c1, c2 = lst[0], lst[1]
    else:
        c1, c2 = '', ''
    try:
      num1 = float(c1)
    except ValueError:
        print('неверный формат 1-го числа')
        num1 = 0
    try:
      num2 = float(c2)
    except ValueError:
        print('неверный формат 2-го числа')
        num2 = 0
    if opr == "+":
        res = num1 + num2
    elif opr == '-':
        res = num1 - num2
    elif opr == '*':
        res = num1 * num2
    elif opr == '/':
        if num2 == 0:
            print('Деление на 0 !')
        else:
            res = num1 / num2
    else:
        print('Неопределенная операция!')
    print(f'Результат: {res}')
