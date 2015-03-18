# coding: utf-8
N, M = map(int, raw_input().split())
rel = [[i == j for i in range(N)] for j in range(N)]
for i in range(M):
  a, b = map(int, raw_input().split())
  rel[a - 1][b - 1] = True
  rel[b - 1][a - 1] = True

ans = 0
# 派閥に参加する人の組み合わせをbitを立てて全通り調べる。
for i in range(1 << N + 1):
  n = 0
  # この組み合わせで派閥が成立するかをチェック。
  for a in range(N):
    if i & (1 << a):
      n += 1
    fail = False
    for b in range(N):
      if i & (1 << a) and i & (1 << b):
        if not rel[a][b]:
          fail = True
          break
    if fail:
      break 
  else:
    ans = max(ans, n)
print ans
