N, D, K = map(int, input().split())
d = [tuple(map(int, input().split())) for i in range(D)]

for i in range(K):
    s, t = map(int, input().split())
    l, r = s, s
    for j, v in enumerate(d):
        if v[0] <= l <= v[1] or v[0] <= r <= v[1]:
            l = min(l, v[0])
            r = max(r, v[1])
        if l <= t <= r:
            print(j + 1)
            break
