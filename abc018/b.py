S = list(input())
N = int(input())
for i in range(N):
    l, r = map(int, input().split())
    S[l - 1:r] = reversed(S[l - 1:r])
print(''.join(S))
