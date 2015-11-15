n = int(input())
s = input()
if n % 2:
    print(-1)
    exit()
s1 = s[:n // 2]
s2 = s[n // 2:]
a = 0
for i in range(n // 2):
    if s1[i] != s2[i]:
        a += 1
print(a)
