INF = 1000000000
N, M = map(int, input().split())
mem = [[INF for i in range(N)] for j in range(N)]

for i in range(M):
    a, b, t = map(int, input().split())
    mem[a - 1][b - 1] = mem[b - 1][a - 1] = t

al = INF
an = -1
for s in range(N):
    ml = 0
    done = [False] * N
    l = [INF] * N
    l[s] = 0
    while True:
        d = -1
        for i in range(N):
            if (d == -1 or l[i] < l[d]) and not done[i]:
                d = i
        if d == -1:
            break
        done[d] = True
        for i in range(N):
            l[i] = min(l[i], l[d] + mem[d][i])
        ml = max(ml, l[d])
    if al > ml:
        an = s
        al = ml
print(al)
