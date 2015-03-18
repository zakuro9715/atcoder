n, c = map(int, input().split())
a = (int(input()) for i in range(n))
v = [[0] * 11, [0] * 11]
for i, a in enumerate(a):
  v[i % 2][a] += 1
f = lambda x: -x[1]
even, odd = sorted(enumerate(v[0]), key=f), sorted(enumerate(v[1]), key=f)
if even[0][0] == odd[0][0]:
  print((n - even[0][1] - max(even[1][1], odd[1][1])) * c)
else:
  print((n - even[0][1] - odd[0][1]) * c)
