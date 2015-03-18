def f(a, i, j, b):
  a, b = list(a), list(b)
  a[i], a[j] = a[j], a[i]
  n = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      n += 1
  return n

N, K = map(int, input().split())
S = input()
a, sl = [], list(S)
for i in range(N):
  ssl = sorted(list(sl))
  d = sl[0]
  for c in ssl:
    p = sl.index(c)
    if f(a + sl, i, p + i, S) <= K:
      sl[0], sl[p] = sl[p], sl[0]
      d = c
      break
  sl.remove(d)
  a.append(d)
print(''.join(a))
