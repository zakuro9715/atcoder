N, A, B = map(int, input().split())
print(A * N - (A - B) * min(5, N))
