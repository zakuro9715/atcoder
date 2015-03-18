A, K = input().split()
K = int(K)
m = [False] * 10

s = []
for i, a in enumerate(A):
    na = int(a)
    if m[na]:
        s.append(0)
    elif K:
        s.append(0)
        K -= 1
        m[na] = True
    else:
        for i in range(10):
            if
