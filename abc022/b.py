N = int(input())
m = {}
ans = 0
for i in range(N):
    a = int(input())
    if a in m:
        ans += 1
    m[a] = True
print(ans)
