N, M = map(int, input().split())
aji = [0] + [int(input()) for i in range(N)]
aji[0] = aji[2]

ca = 1
dp = [1] + [0] * N
l = 0
mem = [0] * (M + 1)
for i, v in enumerate(dp):
    if i == 0:
        continue
    if l != mem[aji[i]]:
        l = mem[aji[i]]
        ca = 0
        for j in range(l, i):
            dp[i] = (dp[i] + dp[j]) % 1000000007
    else:
        dp[i] = ca
    ca += dp[i]
print(dp[-1])
