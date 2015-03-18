N = int(input())
m = map(lambda x: int(x) - 2, input().split())
a = 0
for v in m:
  while not (v % 3 and v % 2):
    a, v = a + 1, v - 1
print(a)
