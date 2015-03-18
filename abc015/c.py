from itertools import combinations
from functools import reduce
N, K = map(int, input().split())

m = []
for i in range(N):
    m.extend(map(int, input().split()))

for v in combinations(range(N * K), N):
    for i in range(N):
        if v[i] // K != i:
            break
    else:
        if reduce(lambda a, b: a ^ b, map(lambda x: m[x], v)) == 0:
            print('Found')
            break
else:
    print('Nothing')
