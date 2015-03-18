def f():
    global a, b
    for i in range(N):
        if a[i] != b[i]:
            x, y = a[i], b[i]
            if a[i].isdigit():
                x, y = y, x
            a = a.replace(x, y)
            b = b.replace(x, y)
            return True
    return False

N = int(input())
a, b = input(), input()
m = 0

while f():
    pass

d = set()
for i in range(N):
    d.update(filter(lambda x: not x.isdigit(), (a[i], b[i])))

ans = pow(10, len(d))
if a[0] == b[0] and not a[0].isdigit():
    ans = ans // 10 * 9
else:
    if not a[0].isdigit():
        ans = ans // 10 * 9
    if not b[0].isdigit():
        ans = ans // 10 * 9

print(ans if ans > 0 else 1)
