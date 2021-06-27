a1, b1 = ['A', '2'],  ['C', '4', 'F']


def hc_to_decimal(ch, ord_1=48, ord_2=65):

    if '0' <= ch <= '9':
        res = ord(ch) - ord_1
    else:
        res = ord(ch) - ord_2 + 10
    return res


def decimal_to_hc(dex, ord_1=48, ord_2=65):

    if 0 <= dex <= 9:
        res = chr(dex + ord_1)
    else:
        res = chr(dex + ord_2 - 10)
    return res


# сложение двух десятичных по модулю 16, в e - разряд переноса: 0 или 1
def sum_dex(a, b, e):
    ad = hc_to_decimal(a)
    bd = hc_to_decimal(b)
    cd = ad + bd + e
    if cd <= 16:
        return [decimal_to_hc(cd), 0]
    else:
        return [decimal_to_hc(cd - 16), 1]


# сложение 2-х шестн. чисел
def sum_hex(a, b):
    res = []
    e = 0
    if len(a) > len(b):
        for i in range(0, len(a) - len(b)):
            b.insert(0, '0')
    elif len(b) > len(a):
        for i in range(0, len(b) - len(a)):
            a.insert(0, '0')
    for i in range(len(a) - 1, -1, -1):
        el1, el2 = a[i], b[i]
        c = sum_dex(el1, el2, e)
        res.insert(0, c[0])
        e = c[1]
    if e == 1:
        res.insert(0, '1')

    return res


# оптимально было бы сделать таблицу умножения аналонично sum_dex,
# но сделано через сложение необходмое количество раз
def mul_hex(a, b):
    res1 = ['0']
    mn = 1
    for i in range(len(b) - 1, -1, -1):
        el = b[i]
        cnt = hc_to_decimal(el) * mn
        res = ['0']
        for j in range(0, cnt):
            res = sum_hex(res, a)
        res1 = sum_hex(res1, res)
        mn *= 16
    return res1


print(sum_hex(a1, b1))
print(mul_hex(a1, b1))
