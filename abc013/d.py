N, M, D = map(int, input().split())
T = [[i for i in range(N)] for j in range(20)]
A = list(map(int, input().split()))

for a in A:
    T[0][a], T[0][a - 1] = T[0][a - 1], T[0][a]

print(T[0])
nn = 2
n = 1
while nn < D:
    for i in range(N):
        T[n][i] = T[n - 1][T[n - 1][i]]
    print(T[i])
    n += 1
    nn = pow(2, n)
