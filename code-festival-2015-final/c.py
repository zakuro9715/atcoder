n = int(input())
s = list(input())
i = 0
a = 0
while i < n * 2:
    if i == n * 2 - 1:
        a += 1
        break
    if s[i] == s[i + 1]:
        i += 1
        a += 1
        continue
    else:
        i += 2
        continue
print(a // 2)
