N, K, M, R = map(int, input().split())
s = list(sorted([int(input()) for i in range(N - 1)]))
if N == K:
    s = [0] + s
else:
    s = s[N - 1 - K:]
if sum(s) >= R * K:
    print(0)
else:
    s[0] = M
    ss = sum(s)
    if ss < R * K:
        print(-1)
    else:
        print(M - (ss - R * K))
