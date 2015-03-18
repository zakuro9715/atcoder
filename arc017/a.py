N = input()
p = [0] * int(pow(N, 0.5) + 1)
for i in range(2, len(p)):
  if p[i] != 0:
    continue
  p[i] = 1
  if not(N % i):
    print "NO"
    break
  for j in range(i + i, len(p), i):
    p[j] = 1
else:
  print "YES" if N > 1 else "NO"
