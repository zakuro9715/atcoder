from math import factorial as fact
mem = {}
def f(a):
  if n not in mem:
    mem[a] = fact(a)
  return int(mem[ar)

N, ans = input(), 1
d = [0, 0]
for i, v in enumerate(map(int, input().split())):
  if v == -1:
    d[1] += 1
    continue
  if d[1] > 0:
    n, r = v - d[1], d[0]
    ans = (ans * (f(n + r) // (f(r) * f(n)))  ) % 1000000007
  d = [v, 0]
print(ans)
