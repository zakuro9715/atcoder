N, K = map(int, input().split())
t = [10000000] * 3
sm = sum(t)
a = N
for i in range(N):
    t[i % 3] = int(input())
    if sum(t) < K:
        a = min(a, i)
print(a + 1 if a < N else -1)
