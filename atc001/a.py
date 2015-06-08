dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
H, W = map(int, input().split())
m = [list(input()) for i in range(H)]
d = [[False for x in range(W)] for y in range(H)]
q = []
for y in range(H):
    for x in range(W):
        if m[y][x] == 's':
            q.extend((x, y))
while q:
    x, y = q.pop(0), q.pop(0)
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 <= xx < W and 0 <= yy < H and m[yy][xx] != '#' and not d[yy][xx]:
            q.append(xx)
            q.append(yy)
            if m[yy][xx] == 'g':
                print('Yes')
                exit()
            d[yy][xx] = True
print('No')
