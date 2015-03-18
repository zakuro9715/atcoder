from itertools import chain
from math import sqrt
N = int(input())
s = sum(list(chain.from_iterable(
        [[N // i, i] for i in range(1, int(sqrt(N)) + 1) if not(N % i)]))) // 2
if s == N:
        
