N = eval(input()) + 1
D = [[0] * N for i in range(N)]
for i in range(1, N):
  l = list(map(int, input().split()))
  for j in range(1, len(l) + 1):
    D[i][j] = l[j - 1] + D[i - 1][j] + D[i][j - 1] - D[i - 1][j - 1]

DP = [0] * N ** 2
for y1 in range(N):
  for x1 in range(N):
    for y2 in range(y1 + 1, N):
      for x2 in range(x1 + 1, N):
        s = (x2 - x1) * (y2 - y1)
        DP[s] = max(DP[s], D[y2][x2] - D[y2][x1] - D[y1][x2] + D[y1][x1])
for i in range(1, len(DP)):
  DP[i] = max(DP[i], DP[i - 1])

for i in range(eval(input())):
  print(DP[eval(input())])
