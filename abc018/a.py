a, b, c = (int(input()) for i in range(3))
if a > b:
    if b > c:
        x = (1, 2, 3)
    elif a > c:
        x = (1, 3, 2)
    else:
        x = (2, 3, 1)
else:
    if b < c:
        x = (3, 2, 1)
    elif a < c:
        x = (3, 1, 2)
    else:
        x = (2, 1, 3)
for v in x:
    print(v)
