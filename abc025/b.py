N, A, B = map(int, input().split())
x = 0

for i in range(N):
    s, d = input().split()
    d = int(d)
    if s[0] == 'E':
        x += max(A, min(d, B))
    else:
        x -= max(A, min(d, B))
if x > 0:
    print('East', end=' ')
if x < 0:
    print('West', end=' ')
print(abs(x))
