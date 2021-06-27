import time


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
        memory[n] = r
        return r
    return g


@memorize
def f(n):
  if n < 2:
     return n
  return f(n - 1) + f(n - 2)


start = time.time()
print(f'{f(32)}')
print(f'{(time.time() - start) * 1000}')  # msec