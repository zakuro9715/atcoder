import math

def t(sx, sy, tx, ty, v):
  return math.sqrt(pow(sx - tx, 2) + pow(sy - ty, 2)) / v

sx, sy, tx, ty, T, V = map(int, input().split())
N = int(input())

a = False
for i in range(N):
  x, y = map(int, input().split())
  a |= t(sx, sy, x, y, V) + t(x, y, tx, ty, V) <= T
print('YES' if a else 'NO')
