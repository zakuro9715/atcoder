N, T = map(int, input().split())

b = int(input())
n = 0
for i in range(N - 1):
    a = int(input())
    n += min(a - b, T)
    b = a
print(n + T)
