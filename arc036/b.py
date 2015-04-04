N = int(input())
h = [int(input()) for i in range(N)]

a = [0] * len(h)
b = [0] * len(h)

for i in range(1, len(h)):
    if h[i] > h[i - 1]:
        a[i] = a[i - 1] + 1
    if h[-i - 1] > h[-i]:
        b[-i - 1] = b[-i] + 1
print(max(map(sum, zip(a, b))) + 1) 
