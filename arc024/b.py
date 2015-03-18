def ts(l):
  s = ['1' if v else '0' for v in l]
  return ''.join(s)

N = int(input())
C = [int(input()) == 1 for i in range(N)]
mem = []

cl, cn = [-1] * N, 1
f = True
d = 0
while cn:
  cn = 0
  v = ts(C)
  if v in mem:
    break
  mem.append(v)
  
  for i in range(N):
    a, b, c = (i - 1) % N, i % N, (i + 1) % N
    if C[a] == C[b] == C[c]:
      cl[cn] = b
      cn += 1
  for i in range(cn):
    C[cl[i]] = not C[cl[i]]
  d += 1

else:
  print(d)
  exit()
print(-1)
