import math
A, B = map(int, input().split())
A, B = min(A, B), max(A, B)

for i in range(int(input())):
    C, D = map(int, input().split())
    rad = math.atan(C / D)
    h = C - A * math.cos(rad)
    w = D - A * math.sin(rad)
    if (h >= B * math.sin(rad) and w >= B * math.cos(rad) or
        min(C, D) >= A and max(C, D) >= B):
        print('YES')
    else:
        print('NO')
