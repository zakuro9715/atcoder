N, M = map(int, input().split())
f = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    f[a].append(b)
    f[b].append(a)

for i in range(N):
    ff = set()
    for j in f[i]:
        ff = ff.union(set(f[j]))
    ff = ff.difference(set(f[i]))
    print(max(0, len(ff) - 1))
