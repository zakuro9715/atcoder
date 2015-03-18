def dfs(n, en, x):
  if n == en:
    return {x : 1}
  dic1 = dfs(n + 1, en, x) 
  dic2 = dfs(n + 1, en, x + W[n])
  for k, v in dic2.items():
    if k in dic1:
      dic1[k] += v
    else:
      dic1[k] = v
  return dic1
 
N, X = map(int, raw_input().split())
W = [0] * N
for i in range(N):
  W[i] = input()
dic1 = dfs(0, N / 2, 0)
dic2 = dfs(N / 2, N, 0)
ans = 0
for k, v in dic1.items():
  if X - k in dic2:
    ans += v * dic2[X - k]
print ans
