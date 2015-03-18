H, W, K = map(int, input().split())

if H > 50 or W > 50:
    exit()

m = [input() for y in range(H)]
ans = 0
for y in range(K - 1, H - K + 1):
    for x in range(K - 1, W - K + 1):
        f = True
        for xx in range(-K, K):
            for yy in range(-K, K):
                if abs(xx) + abs(yy) >= K:
                    continue
                if m[y + yy][x + xx] == 'x':
                    f = False
        if f:
            ans += 1
print(ans)
