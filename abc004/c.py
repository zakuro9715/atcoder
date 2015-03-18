N = input()
c = [1, 2, 3, 4, 5, 6]
for i in range(6):
  c[i] = (N / 5 % 6 + i) % 6 + 1
for i in range(N % 5):
  c[i], c[i + 1] = c[i + 1], c[i]
print ''.join(map(str, c))
