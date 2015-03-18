N = int(input())
d = dict()
for i in range(N):
  s = input()
  d[s] = d.get(s, 0) + 1
print(max(d.items(), key=lambda x:x[1])[0])
