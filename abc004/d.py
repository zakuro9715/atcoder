def arithmetic_series(n):
  return (n + 1) * n / 2

def red(p):
  if abs(-100 - p) >= (R - 1) / 2:
    return arithmetic_series((R - 1) / 2) + arithmetic_series((R - 1) / 2
  return arithmetic_series(abs(-100 - p)) + arithmetic_series(R - abs(-100 - p) - 1)

def blue(p):
  if 100 - p >= B / 2:
    return arithmetic_series(B / 2) * 2
  return arithmetic_series(abs(100 - p)) + arithmetic_series(B - abs(100 - p) - 1)

def green(l, r):
  return arithmetic_series(abs(l)) + arithmetic_series(abs(r))

def cal(p):
  p1, p2 = p - (G - 1), p
  print "%d %d %d" % (red(p1), green(p1, p2), blue(p2))
  return green(p1, p2) + red(p1) + blue(p2)

R, G, B = map(int, raw_input().split())
m = 10000000000
for i in range(G):
  m = min(m, cal(i))
print m
