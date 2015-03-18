def dfs(n, st, fr):
    x = 0
    for c in node[n]:
        if c == fr:
            continue
        x += dfs(c, st, n)
    if n == st:
        return x
    if x == 0:
        return x + h[n]
    return x + 1

n, x = map(int, input().split())
x -= 1
h = list(map(int, input().split()))

node = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    node[a].append(b)
    node[b].append(a)
print(dfs(x, x, -1) * 2)
