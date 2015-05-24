a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
n = 0
if s + t >= k:
    n -= c * (s + t)
print(s * a + t * b - (0 if s + t < k else c * (s + t)))
