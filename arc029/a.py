N = int(input())
a = [int(input()) for i in range(N)]

if N == 1:
    print(a[0])
    exit()
if N == 2:
    print(max(a[0], a[1]))
    exit()
if N == 3:
    print(min(
        max(a[0] + a[1], a[2]),
        max(a[1] + a[2], a[0]),
        max(a[2] + a[0], a[1])
    ))
    exit()
if N == 4:
    print(min(
        max(a[0] + a[1] + a[2], a[3]),
        max(a[1] + a[2] + a[3], a[0]),
        max(a[2] + a[3] + a[0], a[1]),
        max(a[3] + a[0] + a[1], a[2]),
        max(a[0] + a[1], a[2] + a[3]),
        max(a[0] + a[2], a[1] + a[3]),
        max(a[0] + a[3], a[1] + a[2]),
    ))
