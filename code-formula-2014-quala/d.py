S = input()
K = input()
N = len('1234567890abcdefghijklmnopqrstuvwxyz') - len(K)
M = 0
X = 0
for c in S:
    if c in K:
        continue
    v = (N - X - 1) / 2
    M += v
    X += v + 1
print(M * 2 + len(S))
