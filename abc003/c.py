N, K = map(int, raw_input().split())
R = sorted(map(int, raw_input().split()))
ans = 0
for i in range(N - K, N):
  ans = (ans + R[i]) / 2.0
print ans
