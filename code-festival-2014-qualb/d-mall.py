N = int(input())
H = [int(input()) for i in range(N)]
for i in range(N):
    n = 0
    for j in range(i + 1, N):
        if H[i] >= H[j]:
            n += 1
        else:
            break
    for j in range(i - 1, -1, -1):
        if H[i] >= H[j]:
            n += 1
        else:
            break
    print(n)
