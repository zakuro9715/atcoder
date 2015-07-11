H, W = map(int, input().split())
m = [list(map(int, input())) for i in range(H)]
d = [[0 for x in range(W)] for y in range(H)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for y in range(1, H - 1):
    for x in range(1, W - 1):
        n = 100000
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            n = min(n, m[yy][xx])
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            m[yy][xx] -= n
        d[y][x] += n
print('\n'.join([''.join(map(str, d[i])) for i in range(H)]))
