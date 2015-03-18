R, L = map(int, input().split())
r = sorted(map(int, input().split()))
l = sorted(map(int, input().split()))
a = 0
while len(r) and len(l):
  if r[0] == l[0]:
    r, l = r[1:], l[1:]
    a += 1
  elif r[0] < l[0]:
    r = r[1:]
  else:
    l = l[1:]
print(a)
