def dfs(i, n):
    if i == 0:
        return n
    children = v[i]
    res = 0
    for ch in children:
        res = max(res, dfs(ch, n + 1))
    return res
N, M = map(int, input().split())
v = [[] for i in range(N)]
root = [True] * N

for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    v[a].append(b)
    root[b] = False

ans = 0
for i in range(N):
    if not root[i]:
        continue
    ans = max(ans, dfs(i, 1))
print(ans)
