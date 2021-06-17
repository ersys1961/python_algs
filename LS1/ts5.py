keys = [str(i) for i in range(32, 128)]
chars = [chr(i) for i in range(32, 128)]
rest = len(chars)
ptr = 0
while rest > 0:
    if rest >= 10:
        l1 = 10
    else:
        l1 = rest
    rest -= l1
    s = ''
    for i in range(ptr, ptr + l1):
        s = s + '  ' + keys[i] + ': "' + chars[i] + '"'
    print(s)
    ptr += l1
