n, x = 0, []
for i, v in enumerate(input().split()):
    if v == 'not':
        n += 1
    else:
        if n % 2:
            x.append('not')
        n = 0
        x.append(v)
if n:
    x.extend(['not'] * n)
print(' '.join(x))
