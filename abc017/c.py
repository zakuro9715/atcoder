N, M = map(int, input().split())
wa = [0] * (M + 1)
s = 0
for a, b, c in [map(int, input().split()) for i in range(N)]:
    wa[a - 1] += c
    wa[b] -= c
    s += c
m = wa[0]
for i in range(1, M):
    wa[i] += wa[i - 1]
    m = min(m, wa[i])
print(s - m)
