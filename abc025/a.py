from itertools import product
print(''.join(list(sorted(product(input(), repeat=2)))[int(input()) - 1]))
