def f(i):
    while i % 2 == 0:
        i = i // 2
    return i

N = int(input())
s = set()
for i in map(int, input().split()):
    s.add(f(i))
print(len(s))
