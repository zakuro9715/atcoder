m = [0] * 1000002
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    m[a] += 1
    m[b + 1] -= 1

v = 0
ans = 0
for i in m:
    v += i
    ans = max(ans, v)
print(ans)
