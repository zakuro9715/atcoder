a = [0, 0, 1] + [0] * 1000000
for i in range(3, 1000000):
  a[i] = (a[i - 1] + a[i - 2] + a[i - 3]) % 10007
print(a[int(input()) - 1])
