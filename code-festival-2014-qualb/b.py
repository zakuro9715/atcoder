N, K = map(int, input().split())
m = 0
for i in range(N):
    m += int(input())
    if m >= K:
        print(i + 1)
        break
