N, K = map(int, input().split())
S = list(input())
for i in range(K):
  p = S.index(min(S[i:]), i) 
  if p != i:
    S[i], S[p] = S[p], S[i]
    K -= 2
    if K <= 1:
      break
print(''.join(S))
