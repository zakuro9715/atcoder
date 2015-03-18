import itertools

N = int(input())
C = [int(input()) for i in range(N)]

s = 0
for i in range(N):
  m = -1
  for j in range(N):
    m += 1 if C[i] % C[j] == 0 else 0
  if m == 0:
    s += 1.0
  elif m % 2:
    s += 0.5
  else:
    s += (m + 2) / (m * 2 + 2)
print(s)
