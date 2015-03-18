f = lambda x: int(x) - 1
H, W = map(int, input().split())
sy, sx = map(f, input().split())
gy, gx = map(f, input().split())
c = [list(input()) for i in range(H)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))

q = list()
q.append((sx, sy, 0))
c[sy][sx] = '#'
while len(q) > 0:
  x, y, n = q.pop(0)
  if x == gx and y == gy:
    print(n)
    break
  for dx, dy in d:
    tx, ty = x + dx, y + dy
    if c[ty][tx] == '.':
      c[ty][tx] = '#'
      q.append((tx, ty, n + 1))
