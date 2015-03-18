N, K = map(int, raw_input().split())
ab = -1
s = 0
l = 0
for i in range(N):
  a = int(raw_input())
  if a > ab:
    l = l + 1
  else:
    s += max(l - K + 1, 0)
    l = 1
  ab = a
s += max(l - K + 1, 0)
print s


