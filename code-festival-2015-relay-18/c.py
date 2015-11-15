s = '314159265358979'
p = input()
if p == '0':
    print(32)
else:
    for i, c in enumerate(s):
        if c == p:
            print(i)
            exit()
