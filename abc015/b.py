input()
n, m = 0, 0
for v in list(map(int, input().split())):
    if v:
        n += 1
        m += v
print(m // n + (1 if m % n else 0)) 
