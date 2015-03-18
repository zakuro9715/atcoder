R, C, D = map(int, input().split())
A = [[]] * R
for y in range(R):
  A[y] = list(map(int, input().split()))
  for x in range(len(A[y])):
    d = y + x
    if d % 2 != D % 2 or d > D:
      A[y][x] = 0
    
print(max([v for v in A for v in v]))
