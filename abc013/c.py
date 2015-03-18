N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())
B, D = B + E, D + E

M = N * E - H

if M < 0:
    print(0)
    exit()

ans = 1000000000000000000000
for i in range(N):
    # i回普通の食事をとる
    a = M - B * i
    if a < 0:
        ans = min(ans, i * A)
        break
    ans = min(ans, (a // D + 1) * C + i * A)
print(ans)
