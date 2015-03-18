dp = [0, 2] + [0] * 20
for i in range(2, 20):
  dp[i] = dp[i - 1] * 8 + 10 ** i
ans = 0
for i, v in enumerate(input()[::-1]):
  ans += int(v) * dp[i]
print(dp)
print(ans)
