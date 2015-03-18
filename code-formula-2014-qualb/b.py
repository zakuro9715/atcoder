x = [0, 0]
for i, v in enumerate(reversed(list(map(int, input())))):
    x[i % 2] += v
print(x[1], x[0])
