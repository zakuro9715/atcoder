def dfs(n, m):
  if m in NG:
    return False
  if m == 0:
    return True
  if n == 100:
    return False
  if mem[n][m] != -1:
    return mem[n][m]
  mem[n][m] = (
    dfs(n + 1, m) or 
    dfs(n + 1, m - 1) or 
    dfs(n + 1, m - 2) or 
    dfs(n + 1, m - 3))
  return mem[n][m]

N = int(input())
NG = [int(input()) for i in range(3)]
mem = [[-1 for j in range(301)] for i in range(100)]

print('YES' if dfs(0, N) else 'NO') 
