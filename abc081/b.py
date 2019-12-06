input()
s = list(map(int, input().split()))
ans = 0
while True:
    for i, v in enumerate(s):
        if v % 2 != 0:
            break
        s[i] = v / 2
    else:
        ans += 1
        continue
    break
print(ans)
