A, B, C = map(int, input().split())
n = (1 if A + B == C else 0) + (2 if A - B == C else 0)
print(['!', '+', '-', '?'][n])
