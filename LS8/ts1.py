import hashlib

str = input('Введите строку')

set_of_substring = set()

for i in range(len(str)):
    for j in range(len(str), i, -1):
        hash_str = hashlib.sha1(str[i:j].encode('utf-8')).hexdigest()
        set_of_substring.add(hash_str)

print(f'{len(set_of_substring) -1} различных подстрок в строке {str}')