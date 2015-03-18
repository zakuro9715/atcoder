from bisect import bisect

INF = 10000000000
N = int(input())
c = [int(input()) for i in range(N)]
mem = [-INF] + [INF] * N

for i in range(N):
  p = bisect(mem, c[i])
  mem[p] = min(mem[p], c[i])
print(mem.count(INF))
