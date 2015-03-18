def f(s, k):
    s = str(s)
    m = [False] * 10
    for c in s:
        m[int(c)] = True
    return m.count(True) <= k 

A, K = map(int, input().split())
if A > 500000:
    exit()
n = 1000000000
for i in range(A * 2 + 1):
    if f(i, K):
        n = min(n, abs(A - i))
print(n)
