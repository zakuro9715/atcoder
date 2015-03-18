def search(n, m):
  mx = n 
  mn = 0
  while mx - mn > 1:
    mid = (mn + mx) // 2
    if mid * 3 + (n - mid) * 4 == m:
      return mid, n - mid
    if mid * 3 + (n - mid) * 4 < m:
      mx = mid
    else:
      mn = mid
  if mx * 3 + (n - mx) * 4 == m:
    return mx, n - mx
  if mx * 3 + (n - mn) * 4 == m:
    return mn, n - mn
  return -1, -1

N, M = map(int, input().split())
for n in range(0, N + 1):
  a, b = search(N - n, M - n * 2)
  if (a, b) != (-1, -1):
    print(n, a, b)
    exit()
print(-1, -1, -1)
