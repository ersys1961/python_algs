from collections import Counter


class Node(object):
  def __init__(self, symbol='', weight=0):
    self.left = None
    self.right = None
    self.symbol = symbol
    self.weight = weight

  def is_leaf(self):
      return self.left is None and self.right is None


# frequency = {'a': 1, 'b': 3, 'c': 2}
def huffman_tree(frequency):
  nodes = [Node(char, frequency.get(char)) for char in frequency.keys()]
  for _ in range(len(frequency) - 1):
    nodes.sort(key=lambda n: n.weight)  # Переупорядочить все узлы по весу
    left = nodes.pop(0)
    right = nodes.pop(0)
    parent = Node('', left.weight + right.weight)
    parent.left = left
    parent.right = right
    nodes.append(parent)
  return nodes.pop()


def get_codes(root, codes=dict(), code=''):

    if root is None:
        return

    if root.is_leaf():
        codes[root.symbol] = code
        return codes

    get_codes(root.left, codes, code + '0')
    get_codes(root.right, codes, code + '1')

    return codes


def huffman_encoding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


def huffman_decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res


str1 = 'hello python jun'
freq = Counter(str1)
hf_tree = huffman_tree(freq)

codes = get_codes(hf_tree)
print(codes, '\n')

print(str1)
hf_code = huffman_encoding(str1, codes)
print(hf_code)
str2 = huffman_decoding(hf_code, codes)
print(str2)
