import math
def comb(n, r):
  f = math.factorial
  return f(n) / (f(n - r) * f(r))
R, C = map(int, raw_input().split())
X, Y = map(int, raw_input().split())
D, L = map(int, raw_input().split())
area = (R - X + 1) * (C - Y + 1) 
print  area * comb(D + L, D) % 1000000007
