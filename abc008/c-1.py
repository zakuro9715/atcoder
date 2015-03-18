import itertools
import math

N = int(input())
if N > 8:
  exit()
C = [int(input()) for i in range(N)]

s = 0
for c in itertools.permutations(C):
  n = len(c)
  l = [True] * n
  for i in range(n):
    for j in range(i + 1, n):
      if c[j] % c[i] == 0:
        l[j] = not l[j]
  s += l.count(True)

print(s / math.factorial(N))
