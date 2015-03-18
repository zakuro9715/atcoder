import math
N = eval(input())
P = []
ans = 0
for i in range(N):
  P.append(list(map(int, input().split())))
for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      dx, dy = P[i][0], P[i][1]
      s = abs((P[j][0] - dx) * (P[k][1] - dy) - (P[j][1] - dy) * (P[k][0] - dx))
      ans += 1 if s % 2 == 0 and s != 0 else 0
print(ans)
