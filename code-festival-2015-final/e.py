d = {
    (0, 1): '!!',
    (0, -1): '-!!',
    (1, 0): '!',
    (-1, 0): '-!',
}

s = list(reversed(input()))

i = 0
while i < len(s) and s[i] == '-':
    i += 1

if i >= len(s):
    print('-' if len(s) % 2 else '')
    exit()

i += 1

s = s[i:]
a = (1, 0)

for c in s:
    if c == '-':
        a = (a[0] * -1, a[1] * -1)
    if c == '!':
        a = (int(not a[0]), int(not a[1]))
print(d[a])
