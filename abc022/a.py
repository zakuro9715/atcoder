N, A, B = map(int, input().split())
W = int(input());
x = [W]
for i in range(1, N):
    x.append(x[-1] + int(input()))
print(len(list(filter(lambda x: A <= x <= B, x))))
