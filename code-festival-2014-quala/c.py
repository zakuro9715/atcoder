def f(t):
    return not (t % 4) and (t % 100 or not(t % 400)) 

T, n  = 2000, 0
t, B = map(int, input().split())

while t % T and t <= B:
    if f(t):
        n += 1
    t += 1

while t + T <= B:
    n += (100 - 4 + 1) * 5
    t += T

while t <= B:
    if f(t):
        n += 1
    t += 1

print(n)
